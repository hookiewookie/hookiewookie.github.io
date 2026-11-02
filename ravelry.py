def define_env(env):  
    @env.macro  
    def ravelry_block():  
        meta = env.page.meta  
        slug = meta["ravelry_pattern_slug"]  
        cart = env.variables.ravelry_cart_id 
        pid  = meta["ravelry_pattern_id"]  
        return f"""  
Find this pattern on <a href="https://www.ravelry.com/patterns/library/{slug}">Ravelry</a>  
<a href="https://www.ravelry.com/badges/redirect?p={slug}"><img src="https://api.ravelry.com/badges/projects?p={slug}&t=.svg" style="border:none"/></a>  
or buy it here:  
<div class="button-row">  
  <a href="#" class="btn" onclick="R.cart.add({cart}, {pid}); return false;">add to cart</a>  
  <a href="https://www.ravelry.com/purchase/hookiewookie/{pid}" class="btn">buy now</a>  
  <a href="#" class="btn" onclick="R.cart.show({cart}); return false;">cart</a>  
</div>"""

### Usage: 
#   ---  
#   ravelry_pattern_slug: mein-muster  
#   ravelry_cart_id: 12345  
#   ravelry_pattern_id: 67890  
#   ---  
#   
#   # Title
#
#   {{ ravelry_block() }}