'''
我们将以新闻机构为例来展示观察者模式的显示世界场景.
新闻机构通常从不同地点收集新闻,并将其发布给订阅者.

由于信息是实时发送或接收的,所以新闻机构应该尽快向其订户公布该消息.
此外,随着技术的进步,订户不仅可以订阅报纸,而且可以通过其他的形式进行订阅,例如电子邮件,移动设备,
短信或语言呼叫.所以,我们还应该具备在将来减价任意其他订阅形式的能力,以便为未来的新技术做好准备.

* 主题的行为由NewsPublisher类表示;
* NewsPublisher提供了一个供订户使用的接口;
* attach()方法供Observer来注册NewsPublisherObserver,detach()方法用于注销;
* subscriber()方法返回已经使用Subject注册的所有订户的列表;
* notifySubscriber()方法可以用来遍历已向NewsPublisher注册的所有订户;
* 发布者可以使用add_news()方法创建新消息,get_news()用于返回最新消息,并通知观察者;
'''

class NewsPublisher:

    def __init__(self):
        self.__subscribers = []
        self.__latest_news = None
    
    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop() 
    
    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]
    
    def notify_subscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def add_news(self, news):
        self.__latest_news = news
    
    def get_news(self):
        return "Got News:", self.__latest_news

'''
* 在这个例子中Subscriber表示Observer, 他是一个抽象的基类,代表其他ConcreteObeserver;
* Subscriber有一个update()方法,但是它需要由ConcreteObservers实现;
* update()方法是由ConcreteObserver实现的,这样只要由新闻发布的时候,它们都能得到Subject(NewsPublishers)的相应通知.
'''

from abc import ABCMeta, abstractmethod

class Subscriber(ABCMeta):

    @abstractmethod
    def update(self):
        pass



'''
* 在本例中,我们由两个主要Observer,分别是实现订户接口的EmailSubscriber和SMSSSubscriber;
* 除了这两个之外,我们建立了另一个观察者AnyOtherSubscriber,它是用来按时Observers与Subject的松散耦合关系的;
* 每个具体观察者的__init__()方法都是使用attach()方法向NewsPublisher进行注册的;
* 具体观察者的update()方法由NewsPublisher在内部用来通知添加了新的新闻.
'''

class SMSSSubscriber:

    def __init__(self, publisher, id):
        self.publisher = publisher
        self.publisher.attach(self)
        self.id = id

    def update(self):
        print(self.id, '---', type(self).__name__, self.publisher.get_news())

class EmailSubscriber:

    def __init__(self, publisher, id):
        self.publisher = publisher
        self.publisher.attach(self)
        self.id = id
    
    def update(self):
        print(self.id, '---', type(self).__name__, self.publisher.get_news())
    
class AnyOtherSubscriber:

    def __init__(self, publisher, id):
        self.publisher = publisher
        self.publisher.attach(self)
        self.id = id
    
    def update(self):
        print(self.id, '---', type(self).__name__, self.publisher.get_news())
    
if __name__ == '__main__':
    news_publisher = NewsPublisher()
    i = 0
    for Subscribers in [SMSSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        Subscribers(news_publisher, i)
        i = i + 1

    print("\nSubscribers:", news_publisher.subscribers())
    
    news_publisher.add_news('Hello World!')
    news_publisher.notify_subscribers()

    print("\nDetached:", type(news_publisher.detach()).__name__)
    print("\nSubscribers:", news_publisher.subscribers())
    
    news_publisher.add_news('My second news!')
    news_publisher.notify_subscribers()