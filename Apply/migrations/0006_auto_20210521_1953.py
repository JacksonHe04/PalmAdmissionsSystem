# Generated by Django 3.2.3 on 2021-05-21 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apply', '0005_auto_20210521_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='palmapplicant',
            name='birthday',
            field=models.CharField(default='生日', max_length=100, verbose_name='出生日期'),
        ),
        migrations.AlterField(
            model_name='palmapplicant',
            name='city',
            field=models.CharField(default='城市', max_length=100, verbose_name='市'),
        ),
        migrations.AlterField(
            model_name='palmapplicant',
            name='district',
            field=models.CharField(default='街道', max_length=100, verbose_name='区'),
        ),
        migrations.AlterField(
            model_name='palmapplicant',
            name='grade_input',
            field=models.IntegerField(verbose_name='专业排名'),
        ),
        migrations.AlterField(
            model_name='palmapplicant',
            name='journal_name2',
            field=models.CharField(default='0', max_length=100, verbose_name='期刊会议名2'),
        ),
        migrations.AlterField(
            model_name='palmapplicant',
            name='major_input',
            field=models.CharField(default='专业', max_length=100, verbose_name='本科专业'),
        ),
        migrations.AlterField(
            model_name='palmapplicant',
            name='objid',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='编号'),
        ),
        migrations.AlterField(
            model_name='palmapplicant',
            name='paper_name2',
            field=models.CharField(default='0', max_length=500, verbose_name='论文2'),
        ),
        migrations.AlterField(
            model_name='palmapplicant',
            name='phonenumber_input',
            field=models.CharField(default='手机号', max_length=100, verbose_name='手机号码'),
        ),
        migrations.AlterField(
            model_name='palmapplicant',
            name='province',
            field=models.CharField(default='省份', max_length=100, verbose_name='省'),
        ),
        migrations.AlterField(
            model_name='palmapplicant',
            name='time_paper2',
            field=models.CharField(default='0', max_length=100, verbose_name='论文发表时间2'),
        ),
        migrations.AlterField(
            model_name='palmapplicant',
            name='undergraduate_university_input',
            field=models.CharField(choices=[('0', '北京大学'), ('1', '中国人民大学'), ('2', '清华大学'), ('3', '北京航空航天大学'), ('4', '北京理工大学'), ('5', '中国农业大学'), ('6', '北京师范大学'), ('7', '中央民族大学'), ('8', '南开大学'), ('9', '天津大学'), ('10', '大连理工大学'), ('11', '吉林大学'), ('12', '哈尔滨工业大学'), ('13', '复旦大学'), ('14', '同济大学'), ('15', '上海交通大学'), ('16', '华东师范大学'), ('17', '南京大学'), ('18', '东南大学'), ('19', '浙江大学'), ('20', '中国科学技术大学'), ('21', '厦门大学'), ('22', '山东大学'), ('23', '中国海洋大学'), ('24', '武汉大学'), ('25', '华中科技大学'), ('26', '中南大学'), ('27', '中山大学'), ('28', '华南理工大学'), ('29', '四川大学'), ('30', '重庆大学'), ('31', '电子科技大学'), ('32', '西安交通大学'), ('33', '西北工业大学'), ('34', '兰州大学'), ('35', '中国人民解放军国防科技大学'), ('36', '东北大学'), ('37', '郑州大学'), ('38', '湖南大学'), ('39', '云南大学'), ('40', '西北农林科技大学'), ('41', '新疆大学'), ('42', '北京邮电大学'), ('43', '北京交通大学'), ('44', '西安电子科技大学'), ('45', '解放军信息工程大学'), ('46', '北京工业大学'), ('47', '北京科技大学'), ('48', '哈尔滨工程大学'), ('49', '南京航空航天大学'), ('50', '南京理工大学'), ('51', '杭州电子科技大学'), ('52', '合肥工业大学'), ('53', '西南交通大学'), ('54', '重庆邮电大学'), ('55', '解放军理工大学'), ('56', '天津理工大学'), ('57', '山西大学'), ('58', '大连海事大学'), ('59', '长春理工大学'), ('60', '哈尔滨理工大学'), ('61', '燕山大学'), ('62', '华东理工大学'), ('63', '上海大学'), ('64', '苏州大学'), ('65', '中国矿业大学'), ('66', '河海大学'), ('67', '江苏大学'), ('68', '南京信息工程大学'), ('69', '浙江工业大学'), ('70', '安徽大学'), ('71', '中国地质大学'), ('72', '武汉理工大学'), ('73', '暨南大学'), ('74', '深圳大学'), ('75', '西南大学'), ('76', '火箭军工程大学'), ('77', '西北大学'), ('78', '南京邮电大学'), ('79', '江南大学')], default='本科学校', max_length=100, verbose_name='本科院校'),
        ),
    ]
