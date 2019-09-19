from django.db import models


class Files(models.Model):
    file = models.FileField(upload_to='Files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.file.url

    class Meta:
        verbose_name_plural = "Files"
