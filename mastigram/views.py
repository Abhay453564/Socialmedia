from django.shortcuts import render, redirect
from django.db.models import Q
from .models import *

# ----------------------------------------------------
#  HOME PAGE
# ----------------------------------------------------
def home_page(request):
    """
    Displays homepage with latest videos and posts.
    """
    videos = Video.objects.all().order_by('-created_at')
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'masti/home.html', {
        'videos': videos,
        'posts': posts
    })


# ----------------------------------------------------
#  POST PAGE (Shows all posts — no search)
# ----------------------------------------------------
def post_page(request):
    query = request.GET.get('q')
    img = Post.objects.all().order_by('-created_at')

    if query:
        img = img.filter(description__icontains=query)

    return render(request, 'masti/post.html', {
        'img': img,
        'query': query
    })


# ----------------------------------------------------
#  POST LIST (With Search Bar)
# ----------------------------------------------------
def post_list(request):
    """
    Displays posts with optional search filter.
    User can search by description (case-insensitive).
    """
    query = request.GET.get('q')  # get search input
    img = Post.objects.all().order_by('-created_at')

    print("🔍 Search query:", repr(query))  # debug info

    if query:
        # Filter posts that contain query (case-insensitive)
        img = img.filter(
            Q(description__icontains=query)
            # Add more fields here if needed:
            # | Q(name__icontains=query)
            # | Q(account__icontains=query)
        )

        print("Matching posts count:", img.count())
        for post in img:
            print("Match found:", post.description)
    else:
        print(" No query entered, showing all posts")

    return render(request, 'masti/post.html', {
        'img': img,
        'query': query
    })


# ----------------------------------------------------
#  REEL PAGE
# ----------------------------------------------------
def reel_page(request):
    """
    Displays all uploaded reels in reverse order.
    """
    reele = Reel.objects.all().order_by('-created_at')
    return render(request, 'masti/reel.html', {'reele': reele})


# ----------------------------------------------------
#  UPLOAD POST
# ----------------------------------------------------
def uploadpost(request):
    """
    Handles post upload (image + description).
    Redirects to home page after upload or discard.
    """
    if request.method == "POST":
        if "upload" in request.POST:
            description = request.POST.get("description")
            image = request.FILES.get("image")
            Post.objects.create(description=description, image=image)
            return redirect('home_page')
        elif "discard" in request.POST:
            return redirect('home_page')

    return render(request, 'creation/uploadpost.html')


# ----------------------------------------------------
#  UPLOAD REEL
# ----------------------------------------------------
def uploadreel(request):
    """
    Handles reel upload (file + caption).
    Redirects to reel page after upload or discard.
    """
    if request.method == "POST":
        if "upload" in request.POST:
            caption = request.POST.get("caption")
            reel = request.FILES.get("reel")
            Reel.objects.create(caption=caption, reel=reel)
            return redirect('reel_page')
        elif "discard" in request.POST:
            return redirect('home_page')

    return render(request, 'creation/uploadreel.html')


# ----------------------------------------------------
#  UPLOAD VIDEO
# ----------------------------------------------------
def uploadvideo(request):
    """
    Handles video upload (file + title + description).
    Redirects to testing page after upload or discard.
    """
    if request.method == "POST":
        if "upload" in request.POST:
            title = request.POST.get("title")
            v_description = request.POST.get("v_description")
            video = request.FILES.get("video")
            Video.objects.create(title=title, v_description=v_description, video=video)
            return redirect('testing')
        elif "discard" in request.POST:
            return redirect('home_page')

    return render(request, 'creation/uploadvideo.html')


# ----------------------------------------------------
#  UPLOAD STORY (Placeholder)
# ----------------------------------------------------
def uploadstory(request):
    """
    Renders story upload page (feature placeholder).
    """
    return render(request, 'creation/uploadstory.html')

def profile_page(request):
    return render(request, 'masti/profile.html')

def video_page(request):
    return render(request, 'masti/video.html')
