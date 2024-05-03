{
    'name':'',
    'summary':"""Employee """,
    'description':""" Description Employee 
    """,
    'license':'OPL-1','LGPL-3'
    'author':'sudoerp',
    'website':'www.odoo.com',
    'category':'',
    'depends':['hr', 'sudo_hris_employee', 'sudo_hris_attendance', 'sudo_hris_payroll'],
    'data':[
        'data/shift_codes.xml',
        'data/generate_res_users.xml',
        'data/generate_resource_calendar.xml',
        'data/generate_resource_resource.xml',
        'data/generate_hr_contract_type.xml',
        'data/generate_hr_department.xml',
        'data/generate_hr_position.xml',
        'data/generate_hr_job.xml',
        'data/generate_hr_grade.xml',
        'data/generate_hr_payroll_structure_type.xml',
        'data/generate_hr_work_location.xml',
        'data/generate_hr_employee_public.xml',
        'data/generate_hr_employee.xml',
        'data/working_calendar.xml',
        'data/generate_hr_leave_type.xml'



    ],
    'demo':[
    ],
    'application':True,
}