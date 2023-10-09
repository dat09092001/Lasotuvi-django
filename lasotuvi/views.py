from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from lasotuvi.App import lapDiaBan
from lasotuvi.DiaBan import diaBan
from lasotuvi.ThienBan import lapThienBan
from lasotuvi.models import Laso
import datetime,json
def api(request):
    now = datetime.datetime.now()
    hoTen = (request.GET.get('hoten'))
    ngaySinh = int(request.GET.get('ngaysinh', now.day))
    thangSinh = int(request.GET.get('thangsinh', now.month))
    namSinh = int(request.GET.get('namsinh', now.year))
    gioiTinh = 1 if request.GET.get('gioitinh') == 'nam' else -1
    gioSinh = int(request.GET.get('giosinh', 1))
    timeZone = int(request.GET.get('muigio', 7))
    duongLich = False if request.GET.get('amlich') == 'on' else True
    db = lapDiaBan(diaBan, ngaySinh, thangSinh, namSinh, gioSinh,
                   gioiTinh, duongLich, timeZone)
    thienBan = lapThienBan(ngaySinh, thangSinh, namSinh,
                           gioSinh, gioiTinh, hoTen, db)
    laso = {
        'thienBan': thienBan,
        'thapNhiCung': db.thapNhiCung
    }
    my_return = (json.dumps(laso, default=lambda o: o.__dict__))
    return HttpResponse(my_return, content_type="application/json")

def lasotuvi_django_index(request):
    return render(request,"home.html")
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload_laso(request):
    if request.method == 'POST':
        image_data = request.POST.get('image')
        hoten = request.POST.get('hoten')
        ngaysinh = request.POST.get('ngaysinh')
        thangsinh = request.POST.get('thangsinh')
        namsinh = request.POST.get('namsinh')

        laso = Laso(
            image_data=image_data,
            hoten=hoten,
            ngaysinh=ngaysinh,
            thangsinh=thangsinh,
            namsinh=namsinh
        )
        print(laso)
        laso.save()

        return JsonResponse({'error': False, 'message': 'Lưu dữ liệu thành công.'})
    else:
        return JsonResponse({'error': True, 'message': 'Yêu cầu không hợp lệ.'})



# Create your views here.
