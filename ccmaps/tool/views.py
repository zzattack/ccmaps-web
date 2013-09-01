# Create your views here.

def index(request):


def version_check(request):
    latest_program = ProgramVersion.objects.all().order_by('-version')[0]
    template_vars = { 
                     'version': latest.version,
                     'release_date': datetime.strptime(latest.date, "%Y-%m-%d").date(),
                     'release_notes': latest.release_notes,
                     'url': latest.file.url,
                     }
    
    return render_to_response('version_check.xml', template_vars, mimetype="text/xml")

def get_latest(request):
    latest_program = ProgramVersion.objects.all().order_by('-version')[0]
    return HttpResponseRedirect(latest_program.file.url)
