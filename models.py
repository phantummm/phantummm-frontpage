from django.db import models
from django.core.urlresolvers import reverse
from django.utils.timesince import timesince
from datetime import datetime

class Project(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    url = models.URLField(blank=True)
    github = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=60, unique=True)
    fulltext = models.TextField(blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project_page", args=[str(self.slug)])

class Update(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    url = models.URLField(blank=True)
    project = models.ForeignKey(Project, blank=True, null=True,
      on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if(self.project):
            self.project.updated = datetime.now()
            self.project.save()
        super(Update, self).save(*args, **kwargs)

    def get_frontpage_json(self):
        """
        Produces JSON-structured data for use with frontpage app. Returns dict
        with following keys: created, title, description, project, url, timesince
        """
        try: project_url = self.project.get_absolute_url()
        except: project_url = False

        return { 'created': self.created.strftime('%Y-%m-%dT%H:%M:%S'), 'title': self.title,
          'description': self.description, 'project': str(self.project),
          'url': self.url, 'timesince': timesince(self.created),
          'project_url': project_url,
        }
