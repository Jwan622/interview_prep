
url = 'https://squareup.com/gb/en?/t/f_online/d_search/p_google/c_nonbrand/o_g_s_nb_ws_em_uk_sos/u_how_to_start_website/l_gb/dt_alldevice/pr_online_store'

# Each component of the URL query string with an underscore is a tracking parameter.
# Create and print a list of each parameter (capitalized).

# result = []
# split_url = url.split('/')
# for ele in split_url:
#     if "_" in ele:
#         result.append(ele.capitalize())

# print(result)



# Create a function that completes and returns 'https://squareup.com/us/en?/t/...' with 4 arguments.
# Let's call the function url_builder
# The 4 arguments should be:
# partner (p_)
# product (pr_)
# device (dt_)
# base_url
'p_google'

'https://squareup.com/us/en?/t/'

def url_builder(partner, product, device, base_url):
    index_of_last_char = len(base_url) - 1
    if base_url[index_of_last_char] == '/':
        url_list = [base_url[:-1]]
    else:
        url_list = [base_url]
    url_list.append(partner)
    url_list.append(product)
    url_list.append(device)

    return '/'.join(url_list)

asser t(url_builder('p_partner', 'pr_product', 'dt_device', 'https://squareup.com/us/en?/t/')) == 'https://squareup.com/us/en?/t/p_partner/pr_product/dt_device'



# Create a new version of the url_builder that takes a base url and a dictionary
# Let's call this url_builder_dict
# Assume the dictionary can have any number of pairs
# The key indicates the beginning of the parameter and the value indicates the value ie {"pr_": "online_store"} would be pr_online_store in the final output


def url_builder_dict(base_url, builder_dict):
    suffix_list = []
    for k, v in builder_dict.items():
        suffix_list.append(k + v)
    print(suffix_list)
    return base_url + '/'.join(suffix_list)



asser t(url_builder_dict('https://squareup.com/us/en?/t/', {'pr_': 'online_store'})) == 'https://squareup.com/us/en?/t/pr_online_store'


# In your own words and without running, describe what this snippet does and give an example of what one of the entries in funcs might look like



import random
funcs = {

}
for i in range(100):    # i : 0-99 random.randint(2, 5) mught be something lik3
    ints = [random.randint(0, 100) for i in range(random.randint(2, 5))]
    f = "y=" + '+'.join([str(n) for n in ints])
    funcs[f] = sum(ints)

    # say random.randint(2, 5) is 3, then ints will oloo like something like [1,99,4]
    # ints = [1, 99, 4]
    # [str(n) for n in ints] => ['1', '99', '4']
    # '+'.join([str(n) for n in ints]) -> '1+99+4'
    # so then we get y=1+99+4 SO that's what f looks like
    # funcs[f]  assignemnt so { 'y=1+99+4' => 104 }

