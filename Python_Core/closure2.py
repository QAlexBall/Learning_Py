def make_filter(keep):
    def the_filter(file_name):
        file = open(file_name)
        lines = file.readlines()
        file.close()
        filter_doc = [i for i in lines if keep in i]
        return filter_doc
    return the_filter
filter = make_filter("pass")
filter_result = filter("res.txt")
print(filter_result)


def res_filter(keep, file_name):
	file = open(file_name)
	lines = file.readlines()
	file.close()
	filter_doc = [i for i in lines if keep in i]
	return filter_doc

print(res_filter("pass", "res.txt"))