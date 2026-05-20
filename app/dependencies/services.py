from typing import Annotated
from fastapi import Depends
from interfaces.service.iAdminService import IAdminService
from interfaces.service.iAuthService import IAuthService
from interfaces.service.iTaskService import ITaskService
from interfaces.service.iUserService import IUserService
from interfaces.service.iDashboardService import IDashboardService
from services.adminService import AdminServices
from services.authService import AuthService
from services.taskService import TaskService
from services.userService import UserServices
from services.dashboardService import DashboardService

AdminServiceDep = Annotated[IAdminService, Depends(AdminServices)]
AuthServiceDep = Annotated[IAuthService, Depends(AuthService)]
TaskServiceDep = Annotated[ITaskService, Depends(TaskService)]
UserServiceDep = Annotated[IUserService, Depends(UserServices)]
DashboardServiceDep = Annotated[IDashboardService, Depends(DashboardService)]
