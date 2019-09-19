from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import View
from .forms import FileUploadForm
from .models import Files


class FileUploadView(View):
    def get(self, request):
        file_list = Files.objects.all().order_by('-id')

        context = {
            'files': file_list,
        }
        return render(self.request, 'upload/basic_upload.html', context)

    def post(self, request):
        form = FileUploadForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            upload = form.save()
            data = {'is_valid': True, 'name': upload.file.name,
                    'url': upload.file.url, 'upload_time': upload.uploaded_at}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


def clear_database(request):
    for f in Files.objects.all():
        f.file.delete()
        f.delete()
    return redirect(request.POST.get('next'))
