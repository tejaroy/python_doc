import pandas as pd
import os
import sys
import smtplib
from datetime import date
import psycopg2
import boto3
# from tabulate import tabulate
import numpy as np
from prettytable import PrettyTable
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# %%
def generate_iam_rds_token(server, region, port, user, S3_KEY, S3_SECRET):
    s3_conn = boto3.client('rds', region_name=region,
                           aws_access_key_id=S3_KEY,
                           aws_secret_access_key=S3_SECRET)
    pwd = s3_conn.generate_db_auth_token(server, port, user, Region=region)
    return pwd


def dbconn():
    servername = 'eregistrybc.cstofpek7t9e.ap-south-1.rds.amazonaws.com'
    username = 'bcmasteruser'
    dbName = 'eregistrybc'
    region = 'ap-south-1'
    port = '5432'
    pwd = 'Dereg1bn!'
    conn = psycopg2.connect(user=username, password=pwd, host=servername, port="5432", database=dbName)
    return conn


def upload_file_to_s3(localfilepath, filename):
    S3_KEY = 'AKIAZGVBOTG3HRFBGKBA'
    S3_SECRET = '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'
    S3_BUCKET = ''
    s3 = boto3.client('s3', aws_access_key_id=S3_KEY,
                      aws_secret_access_key=S3_SECRET)
    s3.upload_file(localfilepath, S3_BUCKET, filename)


def send_mail_reports(attachments=[], recipients=['Deepak.Singhal@Dvara.com'], tabular_table=None, **kwargs):
    today = str(date.today()).replace('-', '_')
    # sender='ops.eregistry@gmail.com'
    sender = 'ops.eregistry@dvara.com'
    gmail_password = 'Welcome@2021'  # 'Dvara@2021'

    COMMASPACE = ', '
    # recipients = ['eswar.m@dvara.com', 'Deepak.Singhal@Dvara.com'  ]

    # Create the enclosing (outer) message
    outer = MIMEMultipart()
    outer['Subject'] = 'Doordrishti Fin MIS-' + today
    outer['To'] = COMMASPACE.join(recipients)
    outer['From'] = sender
    outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'
    # List of attachments
    # att = '/home/ubuntu/workspace/FRMIS/'+today+'_InputAnalytics.xlsx'
    # att = today+'_InputAnalytics.xlsx'

    # attachments = [att]

    # Add the attachments to the message
    for file in attachments:
        try:
            with open(file, 'rb') as fp:
                msg = MIMEBase('application', "octet-stream")
                msg.set_payload(fp.read())
            encoders.encode_base64(msg)
            msg.add_header('Content-Disposition', 'attachment',
                           filename=os.path.basename(file))
            outer.attach(msg)
        except:
            print("Unable to open one of the attachments. Error: ",
                  sys.exc_info()[0])
            raise

    my_message = tabular_table.get_html_string()

    text = "Hi!"

    html = """\
    <html>
        <head>
        <style>
            table, th, td {
                border: 1px solid black;
                border-collapse: collapse;
            }
            th, td {
                padding: 5px;
                text-align: left;    
            }    
        </style>
        </head>
    <body>
    <p>Farmer Summary Details<br>

       %s
    </p>
    </body>
    </html>
    """ % (my_message)

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    email_body = MIMEMultipart("alternative", None, [part1, part2])

    # if kwargs['body']:
    #    email_body=email_body+kwargs['body']
    # body = MIMEText(email_body, 'plain')

    outer.attach(email_body)
    composed = outer.as_string()

    # Send the email
    try:
        with smtplib.SMTP('smtp.office365.com', 587) as s:
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(sender, gmail_password)
            s.sendmail(sender, recipients, composed)
            s.close()
    except Exception as e:
        print("Unable to send the email. Error: ", sys.exc_info()[0])
        raise e
    return 'Mail sent Successfully'



def create_range(start_col='B', no_of_cols=2, start_row=2, end_row=2):
    if no_of_cols > 25:
        r = no_of_cols // 26
        d = no_of_cols - (26 * r)
        end_col = chr(ord('A') + r - 1) + chr(ord('A') + d)
    else:
        end_col = chr(ord('B') + no_of_cols - 1)
    rng = start_col + str(start_row) + ":" + end_col + str(end_row)
    return rng


def create_table(wsheet, rdata, start_position, cell_format, column_format, table_format, table_label,
                 display_data_hdr=True, start_col='B', start_row=2, merge=False):
    end_position = start_position + len(rdata)
    end_position = (
            end_position + 1) if display_data_hdr == True else end_position
    end_position = (end_position + 1) if merge == True else end_position
    end_position = (end_position + 1) if len(rdata) == 0 else end_position

    wsheet.merge_range(create_range(start_col, len(
        rdata.columns), start_position, start_position), table_label, cell_format)
    wsheet.set_row(start_position - 1, 20)
    if merge:
        start_position += 1
    data_range = create_range(start_col, len(
        rdata.columns), start_position + 1, end_position)

    wsheet.add_table(data_range, {
        'header_row': display_data_hdr, 'data': rdata.values, 'columns': column_format})
    wsheet.conditional_format(data_range, table_format)

    return start_position, end_position


def write_to_excel(excelfile, sheet_names, dataframe_objects, date_cols=[], merge_dict={}):
    today = str(date.today()).replace('-', '_')
    try:
        writer = pd.ExcelWriter(excelfile, engine='xlsxwriter', options={
            'remove_timezone': True})
        # Get the xlsxwriter workbook and worksheet objects.
        workbook = writer.book
        # Creating formatting
        header_format = workbook.add_format(
            {'border': 1, 'text_wrap': 1, 'bold': True, 'align': 'left',
             'valign': 'vcenter'})  # , 'border_color':'#72310c'})

        bold_border = workbook.add_format({'border': 6})

        default_table_format = {'type': 'no_blanks', 'format': bold_border}

        right_align_data_format = workbook.add_format(
            {'border': 1, 'text_wrap': 1, 'align': 'right', 'valign': 'vcenter'})

        center_align_data_format = workbook.add_format(
            {'border': 1, 'text_wrap': 1, 'align': 'center', 'valign': 'vcenter'})

        cell_format = workbook.add_format({'align': 'center', 'valign': 'vcenter', 'border': 6,
                                           'bold': 1, 'fg_color': '#a3c614', 'font_size': 12,
                                           'font_color': '#72310c', })
        date_format = workbook.add_format(
            {'num_format': 'mmmm d yyyy', 'border': 1, 'align': 'center', 'valign': 'vcenter'})

        worksheets = []
        merge_sheet = {}
        for name in sheet_names:
            sheet = workbook.add_worksheet(name)
            worksheets.append(sheet)
            if name in merge_dict:
                merge_sheet[sheet] = merge_dict[name]

        # loop through sheets
        for obj in range(len(worksheets)):
            sheet = worksheets[obj]
            if dataframe_objects[obj].empty:
                continue
            data0 = dataframe_objects[obj].copy()
            sheet.set_portrait()
            cols0 = data0.columns
            start_position = 2
            merge = False
            if sheet in merge_sheet:
                i = 1
                for cell_range in merge_sheet[sheet]:
                    sheet.merge_range(
                        cell_range, "Alternative" + str(i), cell_format)
                    i += 1
                merge = True

            # loop trhough this
            column_format = []
            try:
                for col in range(len(cols0)):
                    if cols0[col] in date_cols:
                        column_format.append({'header': cols0[col],
                                              'format': date_format})
                    elif type(data0[cols0[col]].values[0]) == str:
                        column_format.append({'header': cols0[col],
                                              'format': center_align_data_format})
                    else:
                        column_format.append({'header': cols0[col],
                                              'format': right_align_data_format})
            except Exception as e:
                for col in range(len(cols0)):
                    column_format.append({'header': cols0[col],
                                          'format': center_align_data_format})

            start_position, end_position = create_table(sheet, data0, start_position, cell_format,
                                                        column_format, default_table_format,
                                                        sheet_names[obj] + " (" + today + ")", display_data_hdr=True,
                                                        merge=merge)
            for i in range(1, len(cols0) + 1):
                sheet.set_column(i, i, 25)

            sheet.set_row(start_position, 30, cell_format=header_format)

    except Exception as E:
        print("Failed to insert/update record into database table",
              E, sheet_names[obj])
        raise (E)
    finally:
        writer.save()
        writer.close()


query = '''
   with cte as (
    select
        row_number() over (partition by application_id ,
        new_status
    order by
        created_at desc) as rn ,
        application_id ,
        new_status,
        created_at- interval '5:30 hour' created_at
    from
        bl_application_maker_checker_status
    where
        new_status in ('AM', 'CA', 'AF','AD','AA') )
        , cte_2 as (
        select
        row_number() over (partition by application_id,
        new_status 
    order by
        created_at desc) as rn ,
        application_id ,
        new_status,
        remarks,
        created_at- interval '5:30 hour' created_at
    from
        bl_application_maker_checker_status
    where
        new_status in ('AM','CA','RTM','RF') )
    select
        ba.vc_farmer_id as "Farmer Id",
        ba.application_id as "Application Id",
        ba.khetscore_id "Khetscore Id",
        concat(ba2.first_name , '', ba2.last_name ) as "Applicant Name", ba2.phone as "Phone", 
        ca.co_app_name as "Co-Applicant Name", ca.phone as "Co-Applicant Phone",
        ba.fpo_name as "FPO",
        o.org_name "Org Name",
        concat(vf.fr_first_name , '', vf.fr_last_name ) as "FR Name",
        ba2.age "AGE",
        (ba.vc_data ->0->>'total_crop_intent_area'):: varchar "Crop Intent Area",
        case
            when bac.khetscore is null
            or bac.khetscore =-1 then '0'
            else bac.khetscore
        end khetscore,
        (ba.created_at - interval '5:30 hour')::varchar  "Interest Submission Date",
         (ba.submission_date - interval '5:30 hour')::varchar   "Application Submission Date",
        c_am.created_at::varchar  "Approved by maker date",
        c_ca.created_at::varchar  "Approved by checker date",
        c_ad.created_at::varchar  "Approved by checker with deviation",
        c_aa.created_at::varchar  "Application Approved date",
       DATE_TRUNC('minute',(case when c_ad.created_at is null then (c_ca.created_at::timestamp - (ba.submission_date- interval '5:30 hour')::timestamp)  else 
        (c_aa.created_at::timestamp - (ba.submission_date- interval '5:30 hour')::timestamp) end))::varchar  "TAT Login to Checker Approval",
        c_af.created_at "Approved by FI date",
       DATE_TRUNC('minute', (c_af.created_at::timestamp - (ba.submission_date- interval '5:30 hour')::timestamp))::varchar   "TAT Login to Sanction",
        c_am_rm.remarks "Maker Remarks",
        c_am_rm2.remarks "Checker Remarks",
        case when c_am_rm3.application_id is not null then 'NO' else '' end   "FTR",
       c_am_rm3.remarks "Maker’s Remarks where Returned to FR",
       c_am_rm4.remarks "FI User Remarks",
       case when c_am_rm4.application_id is not null then 'YES' else '' end "Rejected by FI user",
        ba.loan_amount "Loan Amount Sought",
        (bac.recommendation_data->0->>'Loan Amount (Approved)'):: integer "Loan Amount Approved",
        balc.loan_category_desc "Loan Category",
        bsm.stage_desc "LOS Stage",
        ba2.district "District",
        ba2.village "Village" ,
        ba2.state "State" ,
        basm.status_desc "Status",
        ba.perdix_status "LMS Status",
        (bac.recommendation_data->0->>'EMI Amount'):: float "EMI",
        case
            when baua.application_id is null then 'NO'
            else 'Yes'
        end as "Deviation",
        baua.deviation "Deviation Details",
        (ba.vc_data ->0->>'total_land_area'):: varchar "Calculated area",
        (bac.application_data->0->>'Area (KhetScore) in acres'):: Varchar "KhetScore Area",
        (bac.credit_report_data ->0->>'credit_score'):: Varchar "Credit Score"
    from
        bl_application ba
    join bl_applicant ba2 on
        ba2.application_id = ba.application_id
    join leads l on
        l.lead_id = ba.lead_id
    join org_fpo_mapping ofm on ofm.fpo_id =l.fpo_id 
    join organization o on o.org_id = ofm.org_id 
    join vc_fr vf on
        vf.fr_id = l.fr_id
    join bl_application_cam bac on
        bac.application_id = ba.application_id
    join bl_application_loan_category balc on
        balc.loan_category = ba.loan_category
    join bl_stage_master bsm on
        bsm.stage_code = ba.application_stage
    join bl_application_status_master basm on
        basm.status_code = ba.application_status
    left join (
        select
            application_id,
            concat(first_name , '', last_name ) co_app_name, phone
        from
            bl_applicant ba3
        where
            lower(type_of_applicant) = 's')ca on
        ca.application_id = ba.application_id
    left join cte c_am on c_am.application_id = ba.application_id  and c_am.new_status = 'AM'  and c_am.rn = 1
    left join cte c_ca on c_ca.application_id = ba.application_id  and c_ca.new_status = 'CA'  and c_ca.rn = 1
    left join cte c_af on c_af.application_id = ba.application_id  and c_af.new_status = 'AF'  and c_af.rn = 1
    left join cte c_ad on c_ad.application_id = ba.application_id  and c_ad.new_status = 'AD'  and c_ad.rn = 1
    left join cte c_aa on c_aa.application_id = ba.application_id  and c_aa.new_status = 'AA'  and c_aa.rn = 1
    left join cte_2 c_am_rm on c_am_rm.application_id=ba.application_id and c_am_rm.new_status = 'AM' and c_am_rm.rn = 1
    left join cte_2 c_am_rm2 on c_am_rm2.application_id=ba.application_id and c_am_rm2.new_status = 'CA' and c_am_rm2.rn = 1
    left join cte_2 c_am_rm3 on c_am_rm3.application_id=ba.application_id and c_am_rm3.new_status = 'RTM' and c_am_rm3.rn = 1
    left join cte_2 c_am_rm4 on c_am_rm4.application_id=ba.application_id and c_am_rm4.new_status = 'RF' and c_am_rm4.rn = 1
    left join (
         select
            application_id ,(string_agg(concat(bbrpm.param_name, ' ',bbrm.param_comp_text),'; ')) deviation
        from
            bl_application_underwriting bau
            join bl_business_rules_param_master bbrpm on bbrpm.param_code=bau.param_code 
			join bl_business_rules_master bbrm on bbrm.param_comp_result=bau.param_result and bau.param_code=bbrm.param_code 
        where
            bau.param_result = 2
            group by application_id) baua on
        baua.application_id = ba.application_id
    where
        lower(ba2.type_of_applicant) = 'p';
    '''


# %%
def convert_decimal_to_int(value):
    try:
        value = int(value)
    except:
        if value == '':
            value = 0
        value = value
    return value


def get_los_pivot(query_df):
    los_pivot = query_df.pivot_table(index=['FR Name'],
                                     columns="Status",
                                     values="Application Id",
                                     aggfunc="count",
                                     margins=True,
                                     fill_value=0)

    reset_los = los_pivot.reset_index()
    los_column = list(reset_los.columns)
    name = query_df.Status.unique()
    where_clause = "'" + "','".join(name) + "'"
    print(where_clause)
    status_master_query = ''' select status_desc from bl_application_status_master
     basm  where status_desc not in ({})'''.format(where_clause)
    try:
        conn = dbconn()
        status_query_df = pd.read_sql_query(status_master_query, dbconn())
    except Exception as e:
        print(e)
    finally:
        conn.close()

    final_columns = ['FR Name', 'Approved by FI User', 'Application Approved', 'Checker Approved', 'Total Approved',
                     'Application Returned To Maker From FR', 'Application Submitted',
                     'Approved by maker and sent to checker', 'Approved with Deviations (by Checker)', 'KYC Pending',
                     'Returned By Maker', 'Rejected by FI User', 'Total under Process',
                     'Checker Rejected', 'Maker Rejected', 'Total Rejected', 'All']

    los_column = list(reset_los.columns)
    for i, d in status_query_df.iterrows():
        column = d['status_desc']
        if column not in los_column:
            print(str(column) + ' --->>newly added with 0 values!')
            reset_los[column] = 0

    for fl in final_columns:
        if fl not in los_column:
            print(fl, ' newly added')
            reset_los[fl] = 0

    reset_los['Total Rejected'] = reset_los['Checker Rejected'] + reset_los['Maker Rejected']

    reset_los['Total Approved'] = reset_los['Approved by FI User'] + reset_los['Application Approved'] + reset_los[
        'Checker Approved']

    reset_los['Total under Process'] = reset_los['Application Returned To Maker From FR'] + reset_los[
        'Application Submitted'] + reset_los['Approved by maker and sent to checker'] + reset_los[
                                           'Approved with Deviations (by Checker)'] + reset_los['KYC Pending'] + \
                                       reset_los['Returned By Maker'] + reset_los['Rejected by FI User']
    reset_los = reset_los[final_columns]
    los_column = list(reset_los.columns)
    tabular_fields = los_column
    tabular_table = PrettyTable()
    tabular_table.field_names = tabular_fields
    for i, lp in reset_los.iterrows():
        lv = []
        for lc in reset_los:
            value = convert_decimal_to_int(lp[lc])
            lv.append(value)
        tabular_table.add_row(lv)
    return reset_los, tabular_table


def warehouse():
    servername = 'vcdev.doordrishti.ai'
    username = 'postgres'
    pw = 'DvaraDev@1234#'
    dbName = 'dwhmis'
    conn = psycopg2.connect(user=username,
                            password=pw,
                            host=servername,
                            port="5432",
                            database=dbName)
    return conn


def get_df_concat(df, initial=0):
    dictionary = {"'": "''"}
    df.replace(dictionary, regex=True, inplace=True)

    if len(df) == 0:
        return df, 'emptyselect', 'empty'
    if initial == 0:
        cols = list(df.columns.values)
        for cl in cols:
            # if df[cl].dtype == 'float64':
            if cl == 'previous_site_id':
                print(cl, ' dtpe is ', df[cl].dtype)
            #     df[cl] = df[cl].fillna(0)
            if df[cl].dtype in ['int64', 'int32', 'float64']:
                df[cl] = df[cl].fillna(0)
            elif df[cl].dtype in ['bool']:
                df[cl] = df[cl].fillna(False)
            elif cl in ['loan_amount_sought', 'loan_amount_approved', 'farmer_id', 'age', 'crop_intent_area',
                        'khetscore', 'calculated_area', 'khetscore_area', 'khetscore']:
                df[cl] = df[cl].fillna('0')
                df[cl] = "'" + df[cl].astype(str) + "'"
            else:
                df[cl] = df[cl].fillna('')
                df[cl] = "'" + df[cl].astype(str) + "'"
            df[cl] = df[cl].astype(str)

        selectfirst = 'SELECT '
        ite = len(cols)
        i = 1
        for cl in cols:
            if i < ite:
                selectfirst += "'noobdossier' " + str(cl) + ','
            elif i == ite:
                selectfirst += "'noobdossier' " + str(cl)
            i += 1
        df['concat'] = pd.Series(df[cols].fillna('').values.tolist()).str.join(",")
        return df, selectfirst, cols


def execute_query(query):
    try:
        conn = warehouse()
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        code = 200
    except Exception as e:
        print(e)
        # print(query)
        code = 500
    finally:
        conn.close()
    return code


def pandas_to_db(df, tocolumns, tablename):
    df['concat'] = "(" + df['concat'] + ")"

    df['rownumber'] = (np.arange(len(df))) + 1
    trows = len(df)
    lendf = True
    offset = 0
    limit = 999
    i = 1
    Querymsg = ''
    code = 1
    while lendf:
        # Ref https://stackoverflow.com/questions/53934470/equivalent-of-limit-and-offset-of-sql-in-pandas
        dfs = df.sort_values(by='rownumber', ascending=True).reset_index(drop=True).loc[offset: offset + limit - 1]
        offset += 999
        dfs['groupbyValue'] = 1
        dfselect = dfs.groupby('groupbyValue', as_index=False).apply(lambda x: ',  '.join(x.concat))
        dfselect = dfselect.reset_index()
        if len(dfs) is None:
            lendf = False
        elif len(dfs) == 0:
            lendf = False
        else:
            insertQ = (dfselect.iat[0, 1])
            N = 10

            finalselect = ' VALUES  ' + str(insertQ)
            addparenttable = finalselect
            insertquery = 'INSERT INTO ' + tablename + '( ' + tocolumns + ') ' + addparenttable
            insertquery = insertquery.replace("'None'", 'NULL')
            insertquery = insertquery.replace("'nan'", 'NULL')
            insertquery = insertquery.replace("'NaT'", 'NULL')
            insertquery = insertquery.replace("'now()'", 'now()')
            # Querymsg, code = query_execution(connection2, insertquery)
            # output=db.session.execute(insertquery)
            # db.session.commit();
            output = execute_query(insertquery)
            print(output)
            print('insert success', str(output))
            # if code == 0:
            #     break;
    return Querymsg


def insert_into_datawarehouse(query_df):
    try:
        rename_dict = {}
        for cn in query_df.columns:
            name = cn.replace(' ', '_').replace('-', '_').replace("'", "")
            name = name.lower()
            rename_dict[cn] = name
        query_df_bk = query_df.copy()
        query_df_bk = query_df_bk.rename(columns=rename_dict)
        query_df_bk['created_at'] = 'now()'
        query_df_bk['updated_at'] = 'now()'
        colsdf = list(query_df_bk.columns)
        df, selectfirst, colsdfc = get_df_concat(query_df_bk)
        colstr = ",".join(colsdf)

        Querymsg = pandas_to_db(df, colstr, tablename='bcmis_lending')
    except Exception as e:
        print(e)


def GenerateMIS():
    try:
        conn = dbconn()
        query_df = pd.read_sql_query(query, dbconn())
        # query_df.to_csv('temp.csv')
        query_df = query_df.where(query_df.notnull(), None)
        cols = [
            "Application Submission Date", "Approved by maker date", "Approved by checker date", "Approved by FI date"
        ]
        for col in cols:
            query_df[col] = query_df[col].astype(str)
    except Exception as e:
        print(e)
    finally:
        conn.close()
    insert_into_datawarehouse(query_df)
    reset_los, tabular_table = get_los_pivot(query_df)
    fr_names = query_df['FR Name'].unique()
    statuses = query_df['Status'].unique()
    headers = ['FR Name'] + list(statuses)
    table = []
    for fr in fr_names:
        row2 = []
        row2.append(fr)
        fr_df = query_df[query_df['FR Name'] == fr]
        for status in statuses:
            sm = fr_df[fr_df['Status'] == status]['Application Id'].value_counts().count()
            row2.append(sm)

        table.append(row2)
    # summary_df=pd.DataFrame(table,columns=headers)
    # email_summary=str(summary_df)
    # email_summary=tabulate(summary_df, headers, tablefmt="pretty")
    # file=open('email.txt','w')
    # print(email_summary,file=file)

    today = str(date.today()).replace('-', '_')
    output_folder = 'MIS_Reports'
    excelfile = os.path.join(output_folder, 'BCMIS_' + today + '.xlsx')
    sheet_names = ['BcLendingMIS']
    dataframes = [query_df]
    try:
        write_to_excel(excelfile, sheet_names, dataframes)
    except Exception as e:
        print(e)
        raise e

    filepath = 'MIS/' + excelfile
    # Upload the file to S3
    # try:
    #     upload_file_to_s3(excelfile, filepath)
    #     S3_filepath.append(filepath)
    # except Exception as e:
    #     print(e)
    attachments = [excelfile]
    recipients = ['AshishKumar.Jha@Dvara.com', 'AshishKumar.Singh@Dvara.com', 'Subhalaxmi.Mohanty@Dvara.com',
                  'Lending.Operations@dvara.com', 'Tharakeswar.g@dvara.com', 'Shashank.das@dvara.com',
                  'shashank.dash@dvara.com', 'vishram.thakur@dvara.com', 'pritamkumar.ray@dvara.com',
                  'bhumanagari.blessy@dvara.com', 'swaet.sikha@dvaratrust.onmicrosoft.com', 'aditya.dhanush@dvara.com',
                  'vasudeva.rao@dvara.com']

    mail_response = send_mail_reports(attachments, recipients, tabular_table=tabular_table)
    os.remove(excelfile)
    print(excelfile)


if __name__ == '__main__':
    GenerateMIS()

# %%
