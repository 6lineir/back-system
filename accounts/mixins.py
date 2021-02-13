from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from .models import User

# class VertifyMixin(): 
#     def dispatch(self, request, *args, **kwargs):
#         if self.request.user.is_superuser:

#         return super(CLASS_NAME, self).dispatch(request, *args, **kwargs)

class AuthorsAccessMixin():
  	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			if request.user.is_superuser or request.user.is_author:
				return super().dispatch(request, *args, **kwargs)
			else:
				return redirect("accounts:profile")
		else:
			return redirect("accounts:login")

class SuperUserAccessMixin():
  	def dispatch(self, request, *args, **kwargs):
		if request.user.is_superuser:
			return super().dispatch(request, *args, **kwargs)
		else:
			raise Http404("You can't see this page :Access Admin.")