# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 03:50
from __future__ import unicode_literals

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20170315_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='node_group_id',
            field=models.PositiveSmallIntegerField(choices=[(1, 'S-Light计划1'), (2, 'S-Light计划2'), (3, 'S-Light计划3'), (4, 'S-Light计划4')], default=1, help_text='settings_custom.py的NODE_GROUPS字段', verbose_name='节点组'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_change_node_group_time',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='最后修改节点组时间'),
        ),
        migrations.AddField(
            model_name='user',
            name='node_group_id',
            field=models.PositiveSmallIntegerField(choices=[(1, 'S-Light计划1'), (2, 'S-Light计划2'), (3, 'S-Light计划3'), (4, 'S-Light计划4')], default=user.models.get_node_group, help_text='settings_custom.py的NODE_GROUPS字段', verbose_name='节点组'),
        ),
        migrations.AlterField(
            model_name='node',
            name='flag',
            field=models.CharField(blank=True, default=None, help_text='us：美国；jp：日本；hk：香港；sg：新加坡；cn：中国；kr：韩国；gb：英国；参考：http://flag-icon-css.lip.is/', max_length=63, verbose_name='节点国旗图标'),
        ),
    ]