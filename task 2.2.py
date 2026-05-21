def make_html_tag(tag_name, content, **attributes):
    attrs_list = []
    for key, value in attributes.items():
        attr_name = 'class' if key == 'class_' else key
        attrs_list.append(f'{attr_name}="{value}"')
    attrs_str = " " + " ".join(attrs_list) if attrs_list else ""
    return f"<{tag_name}{attrs_str}>{content}</{tag_name}>"

print(make_html_tag('p', 'Hello World'))

