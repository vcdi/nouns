import results

import nouns

x = nouns.get_x()


example_templates_folder = nouns.BUILTIN_TEMPLATES_FOLDER


def test_literal_templating():
    templates = nouns.Templates(folders=example_templates_folder, preprocess=x)

    data = "abc"

    rendered = templates.render(data)
    assert rendered == "abc"


def test_iterable_templating():
    templates = nouns.Templates(folders=example_templates_folder, preprocess=x)

    data = "a b c".split()
    rendered = templates.render(data)
    assert rendered == "a\nb\nc"


RENDERED_DICT = """\
<div class="table-wrapper ">
  <table class="mapping-table">
    <thead>
      <tr>
        <th>field</th>
        <th>value</th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>a</td>
        <td>0</td>
      </tr>
      <tr>
        <td>b</td>
        <td>1</td>
      </tr>
      <tr>
        <td>c</td>
        <td>2</td>
      </tr>
    </tbody>
  </table>
</div>"""


def test_dict_templating():
    templates = nouns.Templates(folders=example_templates_folder, preprocess=x)

    data = "a b c".split()
    data = zip(data, range(len(data)))
    data = dict(data)
    rendered = templates.render(data)
    assert rendered == RENDERED_DICT


RENDERED_TABLE = """\
<div class="table-wrapper stylish">
  <table>
    <thead>
      <tr>
        <th>a</th>
        <th>b</th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td style="">NULL</td>
        <td style="background: linear-gradient(to right, transparent 0.0%, #eee 0.0%, #eee 100.0%, transparent 100.0%">2</td>
      </tr>
      <tr>
        <td style="background: linear-gradient(to right, transparent 0.0%, #eee 0.0%, #eee 100.0%, transparent 100.0%">3.5</td>
        <td style=""></td>
      </tr>
    </tbody>
  </table>
</div>"""


def test_table_templating():
    templates = nouns.Templates(folders=example_templates_folder, preprocess=x)

    data = results.Results([dict(a=None, b=2), dict(a=3.5, b="")])

    transformed = x(data, style="stylish")
    transformed["_style"] = x("stylish")

    rendered = templates.render(transformed)
    assert rendered == RENDERED_TABLE


RENDERED_FORM = """\
<form method="POST">
</form>"""


def test_thing_templating():
    templates = nouns.Templates(folders=example_templates_folder, preprocess=x)

    data = [x.thingy(method="POST")]

    rendered = templates.render(data)
    assert rendered == RENDERED_FORM


RENDERED_MAPPING = """\
<div class="table-wrapper ">
  <table class="mapping-table">
    <thead>
      <tr>
        <th>field</th>
        <th>value</th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>name</td>
        <td>rob</td>
      </tr>
    </tbody>
  </table>
</div>"""


def test_convenience_templating():
    s = nouns.template("<script>hello</script>")
    assert s == "&lt;script&gt;hello&lt;/script&gt;"

    s = nouns.template("rob", "hi $_")
    assert s == "hi rob"

    s = nouns.template(dict(name="rob"), "hi $name")

    assert s == "hi rob"

    s = nouns.template(dict(name="rob"))
    assert s == RENDERED_MAPPING
