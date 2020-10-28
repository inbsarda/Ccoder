#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Bhagyashri Sarda");
MODULE_DESCRIPTION("A simple example Linux module.");
MODULE_VERSION("0.01");

static int __init lkm_example_init(void) 
{
	printk(KERN_INFO "Hello, World!");
	return 0;
}

static void __exit lkm_example_exit(void) 
{
	printk(KERN_INFO "Goodbye, World!");
}

module_init(lkm_example_init);
module_exit(lkm_example_exit);
