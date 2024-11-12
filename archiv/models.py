from django.db import models
from browsing.utils import model_to_dict
from django.urls import reverse


class Place(models.Model):
    """A Place"""

    PLACE_TYPES = {"city": "City", "country": "Country", "other": "Something else"}
    name = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="Name",
        help_text="Name of the Place",
    )
    type_of_place = models.CharField(max_length=20, choices=PLACE_TYPES)

    class Meta:
        verbose_name = "Place"
        verbose_name_plural = "Places"
        ordering = [
            "name",
        ]

    def field_dict(self):
        return model_to_dict(self)

    def __str__(self):
        if self.name:
            return f"{self.name}"
        else:
            return f"{self.id}"

    @classmethod
    def get_listview_url(self):
        return reverse("archiv:place_list")

    def get_absolute_url(self):
        return reverse("archiv:place_detail", kwargs={"pk": self.id})


class Person(models.Model):
    """A Person"""

    name = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="Name",
        help_text="Name of the Person",
    )
    place_of_birth = models.ForeignKey(
        "Place",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="place_of_birth_of",
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True,
        verbose_name="Date of birth",
        help_text="Date of birth. Use the first of the month/year if only month or year is known",
    )
    place_of_death = models.ForeignKey(
        "Place",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="place_of_death_of",
    )
    date_of_death = models.DateField(
        blank=True,
        null=True,
        verbose_name="Date of death",
        help_text="Date of death. Use the first of the month/year if only month or year is known",
    )

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"
        ordering = [
            "name",
        ]

    def field_dict(self):
        return model_to_dict(self)

    def __str__(self):
        if self.name:
            return f"{self.name}"
        else:
            return f"{self.id}"

    @classmethod
    def get_listview_url(self):
        return reverse("archiv:place_list")

    def get_absolute_url(self):
        return reverse("archiv:place_detail", kwargs={"pk": self.id})


class Book(models.Model):
    """A Book"""

    name = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="Title",
        help_text="The title of the Book",
    )
    author = models.ManyToManyField(
        "Person",
        blank=True,
        verbose_name="Author",
        help_text="The Author of the Book",
        related_name="author_of",
    )
    place_of_publication = models.ManyToManyField(
        "Place",
        blank=True,
        verbose_name="Publication Place",
        help_text="Publication place of the book",
        related_name="publication_place_of",
    )
    published = models.BooleanField(
        default=True, verbose_name="published", help_text="Is the book public"
    )

    class Meta:
        verbose_name = "Buch"
        verbose_name_plural = "Bücher"
        ordering = [
            "name",
        ]

    def field_dict(self):
        return model_to_dict(self)

    def __str__(self):
        if self.name:
            return f"{self.name}"
        else:
            return f"{self.id}"

    @classmethod
    def get_listview_url(self):
        return reverse("archiv:place_list")

    def get_absolute_url(self):
        return reverse("archiv:place_detail", kwargs={"pk": self.id})
