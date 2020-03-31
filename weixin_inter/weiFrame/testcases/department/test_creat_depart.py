from weiFrame.baseApi.department.department import DeptManagment
import logging


class TestCreateDep:

    def test_create_new_dep(self):
        dept_managment = DeptManagment()
        logging.info(dept_managment)
        dept_managment.create_dept()
        create_res = dept_managment.get_response()
        assert create_res.get('errmsg') == 'created'
