from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.service import Services
from django.views import View


# Create your views here.
class Index(View):

    def post(self, request):
        service = request.POST.get('service')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(service)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(service)
                    else:
                        cart[service]  = quantity-1
                else:
                    cart[service]  = quantity+1

            else:
                cart[service] = 1
        else:
            cart = {}
            cart[service] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        print('service', request.POST.get('service'))
        return redirect('homepage')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store')

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    services = None

    services = Services.get_all_services();

    data = {}
    data['services'] = services

    print('you are : ', request.session.get('email'))
    print('you are : ', services)
    return render(request, 'serviceAll.html', data)


