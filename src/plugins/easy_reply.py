from nonebot import get_bot
from pydantic import BaseModel, Extra
from nonebot import on_message, on_command, on_keyword
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, ArgPlainText, CommandArg, Keyword, EventPlainText
from nonebot.log import logger, default_format

logger.add("devdebug.log",
           rotation="00:00",
           diagnose=False,
           level="INFO",
           format=default_format)
# 范围较大的 on_message，任何消息都会响应
fudu_matcher = on_message(rule=to_me(), priority=5)
# command感觉没什么用
watcher = on_command('fudu', rule=to_me(), aliases={'复读', 'fd'}, priority=3)
# 关键字 on_keyword
key_matcher = on_keyword(keywords={'翻译', 'fanyi', '我测你们码'}, rule=to_me())


# key_matcher = on_message(rule=to_me(), priority=5)


async def tail_msg(txt: str = EventPlainText()):
    pass


# 所有消息都会回复
# 如果没有匹配的handler 则复读接受到的消息^_^
@fudu_matcher.handle()
async def handle_func(txt = EventPlainText()):
    await fudu_matcher.send(f"我是复读机：\n{txt}")



@key_matcher.handle()
async def proto_fanyi(foo: str = Keyword()):
    logger.info('fanyi lets go')
    await key_matcher.finish(f'翻译功能开发中....\n{foo}')
    key_matcher.stop_propagation()
    # await key_matcher.send(raw_arg)


@watcher.handle()
async def handle_fd_func(matcher: Matcher, arg: Message = CommandArg()):
    plain_text = arg.extract_plain_text()
    print(plain_text)
    if plain_text:
        await watcher.finish(f"复读:{plain_text}")
    else:
        await watcher.finish('额')
