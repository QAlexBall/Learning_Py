# 门面模式 ----- 与门面相适

### 理解结构型设计模式
* 结构型模式描述如何将对象和类组合成更大的结构.
* 结构模式是一种能够简化设计工作的模式,因为它能够找出更简单的方法来认识或表示实体之间的关系.在面向对象世界中,实体指的是对象或类.
* 类模式可以通过继承来描述抽象,从而提供更有用的程序接口,而对象模式则描述了如何将对象联系起来从而组合成更大的对象.结构模式是类和对象模式的综合体.

##### 一些结构设计模式的例子
* 适配器模式: 将一个接口转换成客户希望的另一个接口.它视图根据客户端的需求来匹配不同类的接口.
* 桥接模式: 该模式将对象的接口与其实现进行解耦,使得两者可以独立工作.
* 装饰器模式: 该模式允许在运行时或以动态方式为对象添加职责.我们可以通过接口给对象添加某些属性.

### 理解门面设计模式
门面设计模式实际上完成了下列事项.
* 它为子系统中的一组接口提供一个统一的接口,并定义一个高级接口来帮助客户端通过更加简单的方式使用子系统.
* 门面所解决的问题是,如何使用单个接口对象来表示复杂的子系统.实际上,它并不是封装子系统,而是对底层子系统进行组合.
* 它促进了实现与多个客户端的解耦.

##### 门面
* 它是一个接口,它知道某个请求可以交由哪个子系统进行处理.
* 它使用组合将客户端的请求委派给相应的子系统对象.

##### 系统
* 它实现子系统功能,同时,系统由一个类表示.理想情况下,系统应该由一组负责不同任务的类来表示.
* 它处理门面对象分配的工作,但并不知道门面,并且不引用它.

##### 客户端
* 客户端实例化门面的类.
* 为了让子系统完成相应的工作,客户端需要想门面提出请求.

### 最少知识原则
最少知识原则知道我们减少对象之间的交互.
* 在设计系统时,对于创建的每个对象,都应该考察与之交互的类的数量,以及交互的方式
* 遵循这个原则,就能够避免创建许多彼此紧密耦合的类的情况
* 如果类之间存在大量依赖关系,那么系统就会变得难以维护.如果对系统中的任何一部分进行修改,都可能导致系统的其他部分被无意改变,这意味着系统会退化.

##### 迪米特法则
1. 每个单元对系统中其他单元知道的越少越好
2. 单位应该只与朋友交流
3. 单元不应该知道它操作的对象的内部细节
