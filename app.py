pies = [

    {
        'name': 'Pumpkin',
        'price': 10.99,
        'weight': '1lb 12oz',
        'color': 'rgb(240, 156, 29)'
    },

    {
        'name': 'Apple',
        'price': 14.99,
        'weight': '2lb 14oz',
        'color': 'rgb(246, 208, 151)'
    },

    {
        'name': 'Peach',
        'price': 14.99,
        'weight': '3lb 0oz',
        'color': 'rgb(253, 219, 118)'
    },

    {
        'name': 'Cherry',
        'price': 14.99,
        'weight': '2lb 14oz',
        'color': 'rgb(195, 8, 11)'
    },

    {
        'name': 'Blueberry',
        'price': 13.99,
        'weight': '3lb 6oz',
        'color': 'rgb(29, 19, 112)'
    },

    {
        'name': 'Chocolate Pecan',
        'price': 19.99,
        'weight': '2lb 5oz',
        'color': 'rgb(101, 73, 35)'
    }
]


total = None
most_cost_effective = None
pies_by_cost = None
pies_by_weight = None
pies_by_cost_per_pound = None



output = {
    "analysis": {
        "total":total,
        "most_cost_effective":most_cost_effective
    },
    "charts": {
        "pies_by_cost": pies_by_cost,
        "pies_by_weight": pies_by_weight,
        "pies_by_cost_per_pound": pies_by_cost_per_pound
    }
}

# {
    # "labels": x,
    # "datasets":[
    #     {
    #         "data":y, 
    #         "backgroundColor":z
    #     }
    # ]
# }