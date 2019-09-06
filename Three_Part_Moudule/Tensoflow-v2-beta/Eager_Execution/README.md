# Eager Execution

Tensorflow的Eager Execution是一种命令式编辑环境，可立即评估操作，无需构建图：操作会返回具体的值，而不是构建以后再运行的计算图。


The name tf.enable_eager_execution is deprecated. Please use tf.compat.v1.enable_eager_execution instead.

# Object-bases saving

tf.train.Checkpoint can save and restore tf.Variables to and from checkpoints:

```python
x = tf.Variables(10.)
checkpoints = tf.train.Checkpoint(x=x)

x.assign(2.) # Assign a new value to the variables and save.
checkpoint_path = './ckpt/'
checkpoint.save('./ckpt/')

x.assign(11.)  # Change the variable after saving.

# Restore values from the checkpoint
checkpoint.restore(tf.train.latest_checkpoint(checkpoint_path))

print(x)  # => 2.0
```
