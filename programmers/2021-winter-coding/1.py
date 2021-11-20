def solution(character, monsters):
    from math import ceil
    def custom_int(val):
        try:
            tmp = int(val)
            return tmp
        except:
            return val
    character_health, character_atk, character_def = map(int, character.split())
    answer = ''
    best_monster = [0,0,101]
    min_num = 10**-10
    
    for m_idx in range(len(monsters)):
        monster = monsters[m_idx]
        m_name, m_exp, m_health, m_atk, m_def = map(custom_int,monster.split()) 
        c_health, c_atk, c_def = character_health, character_atk, character_def
        
        c_dmg = max(0, c_atk - m_def)
        m_dmg = max(0, m_atk - c_def)
        
        # 플레이어 공격력이 0이면 무한정 반복된다.
        if c_dmg == 0:
            continue
        # 한번에 죽는 경우가 아니면 플레이어는 죽지 않는다.
        if m_dmg >= c_health and m_health >= c_dmg:
            continue
            
        taken_time = ceil(m_health / c_dmg)
        exp_by_time = m_exp / taken_time
        
        if best_monster[0] - exp_by_time > min_num:
            continue
        if abs(best_monster[0] - exp_by_time) < min_num:
            if best_monster[1] >= m_exp:
                continue

        best_monster[0] = exp_by_time
        best_monster[1] = m_exp
        best_monster[2] = m_idx
        answer = m_name
    return answer
solution("10 5 2",	["Knight 3 10 10 3","Wizard 5 10 15 1","Beginner 1 1 15 1"])