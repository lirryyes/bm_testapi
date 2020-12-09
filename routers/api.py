from fastapi import APIRouter
from bm.bluemoon import BluemoonWeb
from utils.schemas import ModerLoginBody,ModerGetCookiesBody
from spider.youdao import GetData

router = APIRouter()


@router.get("/tips")
async def login():
    return BluemoonWeb.getDict()

@router.get("/getdata")
async def getdata():
    return GetData.getData()

@router.post("/login")
async def login(data: ModerLoginBody):
    user = data.user
    password = data.password
    web = BluemoonWeb(user, password)
    return web.res_data


@router.post("/getCookies")
async def getCookies(data: ModerGetCookiesBody):
    url = data.url
    token = data.token
    cookies = BluemoonWeb.getCookies(url, token)
    return cookies

@router.get("/getlogin")
async def getlogin():
    return GetData.getLogin()