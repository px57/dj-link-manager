from django.db import models
from kernel.models.base_metadata_model import BaseMetadataModel

class Link(BaseMetadataModel):
    """
        @description: 
    """
    host = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    queryParams = models.CharField(max_length=255)
    hash = models.CharField(max_length=255)
    full_url = models.CharField(max_length=255)
    counter = models.IntegerField(
        default=0
    )

    def decompose_full_url(self):
        """
            @description: 
        """
        url = self.full_url
        self.host = url.split('://')[1].split('/')[0]
        self.path = '/' + '/'.join(url.split('://')[1].split('/')[1:])
        self.queryParams = '?' + '&'.join(self.path.split('?')[1:]) if len(self.path.split('?')) > 1 else ''
        self.hash = '#' + self.path.split('#')[1] if len(self.path.split('#')) > 1 else ''
        self.path = self.path.split('?')[0].split('#')[0]

    def __str__(self):
        """
            @description:
        """
        return self.host + self.path + self.queryParams + self.hash
    
class LinkOpened(BaseMetadataModel):
    """
        @description: 
    """
    profile = models.ForeignKey(
        'profiles.Profile', 
        related_name='link_opened_profile',
        on_delete=models.CASCADE,
    )

    link = models.ForeignKey(
        'Link', 
        related_name='link_opened_link',
        on_delete=models.CASCADE,
    )

    counter = models.IntegerField(
        default=0
    )

    def __str__(self):
        """
            @description:
        """
        return self.profile + self.link