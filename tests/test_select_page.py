import pytest

@pytest.mark.parametrize('i,result', 
                         [
                             ('2', 'Python'),
                             ('3', 'Ruby'),
                             ('4', 'JavaScript'),
                             ('5', 'Java'),
                             ('6', 'C#'),
                         ])
@pytest.mark.parametrize('page', ['Select'], indirect=True)
def test_select_page(select_page, page, i, result):
    select_page.open(page)
    select_page.click_forms()
    select_page.choise(i)
    select_page.click_sumbit()
    
    assert select_page.check() == result
