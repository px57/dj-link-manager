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