from lxml import etree

# 不包括html标签和body标签

data = """
<div>
    <ul>
        <li class="item-0">first item 测试</li>
        <li class="item-1">second item</li>
        <li class="item-inactive">third item</li>
        <li class="item-1">< a href=" ">fourth item</ a></li>
        <li class="item-0">fifth item</ul>
    </ul>
</div>
"""