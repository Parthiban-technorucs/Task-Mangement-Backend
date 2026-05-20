from fastapi import APIRouter
from api.endpoints import taskRoutes, adminRoute, dashboardRoute, userRoutes, authenticateRoutes
from core.authorization import RoleChecker
from fastapi import Depends
from dependency import get_auth_service

allow_admin = RoleChecker(["admin"])
allow_users = RoleChecker(["admin", "user"])

router = APIRouter()

router.include_router(authenticateRoutes.route, prefix='/auth', tags=['auth'])
router.include_router(taskRoutes.route, prefix='/task', tags=['tasks'], dependencies=[Depends(allow_users)])
router.include_router(adminRoute.route, prefix='/admin', tags=['admin'], dependencies=[Depends(allow_admin)])
router.include_router(dashboardRoute.route, prefix='/dashboard', tags=['dashboard'], dependencies=[Depends(allow_users)])
router.include_router(userRoutes.route, prefix='/user', tags=['users'], dependencies=[Depends(allow_users)])
