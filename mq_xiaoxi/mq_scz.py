import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))  # 创建一个socket

chanel = connection.channel()  # 声明一个管道
chanel.queue_declare(queue='hello')  # 在管道里面声明一个queue
chanel.basic_publish(exchange='',  # 使我们能够确切地指定消息应该到那个队列去
                     routing_key='hello',  # 队列名称
                     body='how are you,ok?',   # 队列内容
                     # properties = pika.BasicProperties(
                     #     delivery_mode= 2,  # 消息持久化， 在投递时指定delivery_mode => 2 (1是非持久化)
                     # )
                     )
print("[x]Start 'hello world'")
connection.close()


