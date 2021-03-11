from django.shortcuts import render
from django.views import View


class ReviewView(View):
    reviews = [
        'Best book I\'ve ever read',
        'Brilliant. What a story!',
        'Intriguing',
        'I recommend this book']  # List of reviews as plain strings

    def get(self, request, *args, **kwargs):
        return render(request, "book/reviews.html", context={"reviews": self.reviews})
