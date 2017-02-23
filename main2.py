def read_input(pizza):
    line = pizza.split('\n')[0]
    line.split(' ')
    videos = line.split(' ')[0]
    endpoints = line.split(' ')[1]
    requests = line.split(' ')[2]
    caches = line.split(' ')[3]
    cachesize = line.split(' ')[4]

    index = 0
    videos_dict = {}
    line = pizza.split('\n')[1]
    for item in line.split(' '):
        videos_dict[index] = item
        index += 1

    line = pizza.split('\n')[2]
    datacenter_latency = []
    datacenter_latency.append(line.split(' ')[0])
    connections = line.split(' ')[1]

    useless = ''
    line = 3

    return pizza, videos, endpoints, requests, caches, cachesize, videos_dict, datacenter_latency, connections

def get_data(lines, endpoints):

    current_line = 2

    endpt_datactr_latency = {}
    endpt_cache_latency = {}
    helper_dict = {}


    for endpt in range(0, int(endpoints)):

        sth = lines[current_line].split(" ")
        no_caches = int(sth[1])
        datacenter_latency = int(sth[0])
        current_line += 1

        #mainthing
        endpt_datactr_latency[endpt] = datacenter_latency
    #    print "endpoint: ", endpt, "no of caches: ", no_caches, "datacenter latency: ", datacenter_latency
        for dataline in range(0, no_caches):
            sth = []
            sth = lines[current_line].split(" ")
            cache = sth[0]
            latency = sth[1].rstrip()

            helper_dict[int(cache)] = int(latency)
        #    print "cache: ", cache, "  latency: ", latency
            current_line += 1
        endpt_cache_latency[endpt] = helper_dict
        helper_dict = {}

    #print "endpoint_to_datacenter_latency dict: ", endpt_datactr_latency
    #print "endpoint_to_cache_latency dict:  ", endpt_cache_latency

    return endpt_datactr_latency, endpt_cache_latency


input_file = raw_input('Enter the filepath of the input data: ')
f = open(input_file)
lines = f.readlines()


pizza_object = open(input_file, 'r')
pizza = pizza_object.read()

input_file, videos, endpoints, requests, caches, cachesize, videos_dict, datacenter_latency, connections = read_input(pizza)
#print "vids: ", videos, "\n", "endpoints: ", endpoints,"\n", "request descriptions: ", requests,"\n", "caches: ", caches,"\n", "cache size:", cachesize,"\n"
#print "vids dict", videos_dict
print get_data(lines, endpoints)
#print 'pizza', pizza
