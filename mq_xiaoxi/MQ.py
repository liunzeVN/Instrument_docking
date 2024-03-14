import body as body
import ch as ch
import meth as meth
import pika

# 连接rabbutmq服务器

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))  # 创建一个socket

channel = connection.channel()  # 声明一个管道

# 2.两边谁先启动谁创建队列

# channel.queue_declare(queue='hello',durable=True) # 持久化队列

channel.queue_declare(queue='hello')  # 在管道里面声明一个queue，因为并不知道那个会先运行


#  一旦有消息就执行该回调函数(比如减库存操作就在这里面)

def callback(ch, method, properties, body):
    print(ch,method,properties)  # ch管道内存对象地址
    print("消费者端收到来自消息队列中的{}成功 %r" % body)

# 数据处理完成，mq收到这个应答就会删除消息
    ch.bassic_ack(delivery_tag = method.delivery_tag)  # 告诉消费者消息处理完成

channel.basic_qos(prefetch_count=1)

channel.basic_consume(  # 消费消息
                      callback,  # 如果收到消息，就调用callback函数来处理消息
                      queue ='hello',  # 你要从那个队列里收消息
                      no_ack = True    # no_ack = True # 一般不写，写的话只要死机，消息丢失
                      )

print('当前mq简单模式正在等待生产者往消息队列塞消息........要退出请按Ctrl+c.....')

channel.start_consuming()  # 一起动就一直运行，开始消费消息
