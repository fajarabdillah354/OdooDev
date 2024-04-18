{
    'name':'',
    'summary':"""Employee """,
    'description':""" Description Employee 
    """,
    'license':'OPL-1','LGPL-3'
    'author':'sudoerp',
    'website':'www.odoo.com',
    'category':'',
    'depends':['hr', 'sudo_hris_employee'],
    'data':[
        'data/generate/generate_department/generate_parent2_department.xml',
        'data/generate/generate_department/generate_parent1_department.xml',
        'data/generate/generate_department/generate_department.xml',
        'data/generate/generate_position/generate_position.xml',
        'data/generate/generate_contract/employee_category.xml',
        'data/generate/generate_job_position/generate_job_position.xml',
        # 'data/generate/generate_contract/employee.xml',
        # 'data/generate/generate_contract/working_schedule_contract.xml',
        # 'data/generate/generate_contract/salary_structur_type.xml',
        # 'data/generate/generate_contract/parent_id_bpjs1.xml',
        # 'data/generate/generate_contract/parent_id_bpjs2.xml',
        # 'data/generate/generate_contract/parent_id_bpjs3.xml',
        # 'data/generate/generate_contract/salary_structure.xml',
        'data/generate/generate_grade/generate_grade.xml',
        # 'data/generate/generate_manager/generate_ref2_manager.xml',
        # 'data/generate/generate_manager/generate_ref1_manager.xml',
        # 'data/generate/generate_coach/generate_ref2_coach.xml',
        # 'data/generate/generate_coach/generate_ref1_coach.xml',
        # 'data/generate/generate_manager/generate_manager.xml',
        # 'data/generate/generate_coach/generate_coach.xml',
        # 'data/generate/generate_contract/hr_response.xml',
        'data/data.xml'
    ],
    'demo':[
        # 'data/hr.employee.csv'
    ],
    'application':True,
}