# encoding:utf-8
from app import queue
from app import rpc

@queue('simple')
def simple(ch, method, props, body):
    print(body)

class Simple():

    def callback(self, ch, method, props, body):
        print(body)

    def declare(self):
        # rpc.declare_queue('simple2', auto_delete=True)
        # rpc.basic_consuming('simple2', self.callback)

        # 或者直接通过declare_default_consuming 声明同时绑定
        rpc.declare_default_consuming('simple2', self.callback)

rpc.register_class(Simple)
rpc.run()
