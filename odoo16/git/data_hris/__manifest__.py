{
    'name':'',
    'summary':"""Employee """,
    'description':""" Description Employee 
    """,
    'license':'OPL-1','LGPL-3'
    'author':'sudoerp',
    'website':'www.odoo.com',
    'category':'',
    'depends':['hr', 'sudo_hris_employee', 'sudo_hris_attendance'],
    'data':[
        'data/generate/generate_department/generate_department.xml',
        'data/generate/generate_position/generate_position.xml',
        'data/generate/generate_grade/generate_grade.xml',
        'data/generate/generate_contract/generate_employee_category.xml',
        'data/generate/generate_job_position/generate_jobposition.xml',
        # 'data/generate/generate_contract/generate_employee.xml',
        # 'data/generate/generate_contract/generate_my_company.xml',
        # 'data/generate/generate_contract/generate_company.xml',
        # 'data/generate/generate_contract/generate_working_schedule.xml',
        # 'data/generate/generate_contract/generate_salary_structur_type.xml',
        # 'data/generate/generate_contract/generate_bpjs_ref3.xml',
        # 'data/generate/generate_contract/generate_bpjs_ref2.xml',
        # 'data/generate/generate_contract/generate_bpjs_ref1.xml',
        # 'data/generate/generate_contract/generate_bpjs.xml',
        # 'data/generate/generate_contract/salary_structure.xml',
        # 'data/generate/generate_contract/generate_hr_response.xml',
        # 'data/generate/generate_contract/generate_contract.xml',
        'data/data.xml',

    ],
    'demo':[
        # 'data/hr.employee.csv'
    ],
    'application':True,
}