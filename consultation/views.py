from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from consultation.models import Consult, Choose, TextResponse

def index(request):
    consullinks = Consult.objects.all()
    return render_to_response('consultation/index.html', {'consullinks': consullinks})

def questions(request, consult_id):
    p = get_object_or_404(Consult, pk=consult_id)
    return render_to_response('consultation/consulting.html', {'consult': p},
                               context_instance=RequestContext(request))

def answers(request, consult_id):
    p = get_object_or_404(Consult, pk=consult_id)
    return render_to_response('consultation/answers.html', {'consult': p})

def cast(request, consult_id):
    p = get_object_or_404(Consult, pk=consult_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choose'])
    except (KeyError, Choice.DoesNotExist):
        return render_to_response('consultation/consulting.html', {
            'consult': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.casts += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('consult_results', args=(p.id,)))

