import tensorflow as tf

x = tf.Variable(10.)
checkpoint = tf.train.Checkpoint(x=x)

x.assign(2.)
checkpoint_path = './ckpt/'
checkpoint.save('./ckpt/')

x.assign(11.)

# Resore values from the checkpoint
checkpoint.restore(tf.train.latest_checkpoint(checkpoint_path))
print(x)

