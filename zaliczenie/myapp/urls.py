from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from myapp.views import (
    KlubPilkarskiViewSet,
    ZawodnikViewSet,
    TrenerViewSet,
    MeczViewSet,
    StatystykiViewSet,
    kluby,  # Funkcja kluby do renderowania strony
)

router = DefaultRouter()
router.register(r"kluby", KlubPilkarskiViewSet)
router.register(r"zawodnicy", ZawodnikViewSet)
router.register(r"trenerzy", TrenerViewSet)
router.register(r"mecze", MeczViewSet)
router.register(r"statystyki", StatystykiViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]

urlpatterns += [
    path("api/token/", obtain_auth_token, name="api_token_auth"),
    path("kluby/", kluby, name="kluby"),  # ✅ Teraz Django znajdzie funkcję kluby!
]
