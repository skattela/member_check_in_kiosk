from django.http import HttpResponse
from .models import CheckIn, Member
from django.views import generic
from django.utils import timezone
from django.shortcuts import get_object_or_404, render, reverse
from django.utils.timezone import localtime, now
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.exceptions import ValidationError
from django.db.models import Q


# Member Views CRUD

@method_decorator(csrf_exempt, name='dispatch')
class MemberCreateView(generic.CreateView):
    mode = Member
    fields = ['first_name', 'last_name', 'member_id', 'card_id']
    template_name = 'member_checkin/member_create.html'

    def get_queryset(self):
        return Member.objects.all()

    def get_success_url(self):
        return reverse('member_checkin:members')


class MembersView(generic.ListView):
    template_name = 'member_checkin/members.html'
    context_object_name = 'members_list'

    def get_queryset(self):
        filter_val = self.request.GET.get('search')
        if filter_val:
            print("f" + filter_val)
            new_context = Member.objects.filter(
                Q(last_name__contains=filter_val) | Q(first_name__contains=filter_val) | Q(
                    member_id__contains=filter_val)).order_by("last_name", "first_name", "member_id")
        else:
            new_context = Member.objects.all().order_by("last_name", "first_name", "member_id")
        return new_context


class MemberView(generic.DetailView):
    model = Member
    template_name = 'member_checkin/member.html'


class MemberUpdateView(generic.UpdateView):
    mode = Member
    fields = ['first_name', 'last_name', 'member_id', "card_id"]
    template_name = 'member_checkin/member_update.html'

    def get_queryset(self):
        return Member.objects.all()

    def get_success_url(self):
        return reverse('member_checkin:members')


class MemberDeleteView(generic.DeleteView):
    mode = Member
    template_name = 'member_checkin/member_delete.html'
    success_url = reverse_lazy('member_checkin:members')

    def get_queryset(self):
        return Member.objects.all()


@method_decorator(csrf_exempt, name='dispatch')
class CheckInCreateView(generic.CreateView):
    mode = CheckIn
    fields = ['member']
    template_name = 'member_checkin/checkin_create.html'

    def get_queryset(self):
        return CheckIn.objects.all()

    def get_success_url(self):
        return reverse('member_checkin:checkins')


class CheckInsView(generic.ListView):
    template_name = 'member_checkin/checkins.html'
    context_object_name = 'checkins_list'

    def get_queryset(self):
        filter_val = self.request.GET.get('search')
        if filter_val:
            print("f" + filter_val)
            new_context = CheckIn.objects.filter(
                Q(member__last_name__contains=filter_val) | Q(member__first_name__contains=filter_val)).order_by(
                "created")
        else:
            new_context = CheckIn.objects.all().order_by("created")
        return new_context


class CheckInView(generic.DetailView):
    model = CheckIn
    template_name = 'member_checkin/checkin.html'


class CheckInDeleteView(generic.DeleteView):
    model = CheckIn
    template_name = 'member_checkin/checkin_delete.html'
    success_url = reverse_lazy('member_checkin:checkins')
