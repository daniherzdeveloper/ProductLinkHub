# Generated by Django 4.2.2 on 2023-07-02 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductLinkHubApp', '0009_alter_product_subcategoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product',
            field=models.TextField(default='<iframe sandbox="allow-popups allow-scripts allow-modals allow-forms allow-same-origin" style="width:120px;height:240px;" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" src="//ws-na.amazon-adsystem.com/widgets/q?ServiceVersion=20070822&OneJS=1&Operation=GetAdHtml&MarketPlace=US&source=ss&ref=as_ss_li_til&ad_type=product_link&tracking_id=ventascubantr-20&language=en_US&marketplace=amazon&region=US&placement=B09VCJ2SHD&asins=B09VCJ2SHD&linkId=06496f016b0152d09af40648935efe92&show_border=true&link_opens_in_new_window=true"></iframe>'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategoria',
            field=models.ManyToManyField(to='ProductLinkHubApp.subcategorias'),
        ),
    ]
