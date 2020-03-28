import shopify

def main():
    ''' main function '''

shop_url = "https://%s:%s@rangsutra-shemadeit.myshopify.com/admin/api/%s" % ("48461b840f5a49ea8d1947fcb22d4804", "3a5dc64fa01688d1a75e02f451723252", '2020-01')
shopify.ShopifyResource.set_site(shop_url)

# Get the current shop

products = shopify.Product.find('4396509560893')
#name = []
#for product in products:
#    name.append(product.title)

name = products.title

print(name)

if __name__ == '__main__':
    main()
