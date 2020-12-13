'''
My first impression... what the hell is this? As all of the problems have been based on some sort of datastructure,
I guess this one is one of the ones I don't know about. Some sort of Tree structure?

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.

Never heard of this before: So I shall use this example to try and help me. -- https://www.python.org/doc/essays/graphs/

I think it will be best to encode the bags.

I don't need to include the bag part. If I do I would need to handle for bag and bags

'''

graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

if graph:
    print(True)

