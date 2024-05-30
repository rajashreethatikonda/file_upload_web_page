from django.shortcuts import render
from .forms import UploadFileForm

def handle_uploaded_file(f):
    # Just read the uploaded file and return the data frame (for further processing if needed)
    import pandas as pd
    data = pd.read_excel(f)
    return data

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            data = handle_uploaded_file(request.FILES['file'])
            return render(request, 'upload_success.html', {'data': data.to_html(index=False)})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

