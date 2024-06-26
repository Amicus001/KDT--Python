
def makingsoulnumber(birthday):
      if birthday == 'E'or birthday =='e':
            birthday = "E"
            return birthday
      else:
            if birthday.isdecimal()!=True:
                  print("생년월일을 8자리 입력해 주세요.")
            else:
                  if len(birthday)==8: #입력된 생년월일이 8자리 숫자라면
                        birthday=map(int,list(birthday)) #생년월일을 한 글자씩 잘라서 정수 한 자리 8개의 리스트로 만들기
                        total = sum(birthday) # 리스트 원소 전체 더하기
                        if total>=22: #합이 22보다 크거나 같으면
                              card= total%10 #카드 값은 일의자리만 떼어 씀.
                        elif total<22: #합이 22보다 작으면
                              card = total #카드 값은 그대로.
                        return card #카드 숫자 리턴
                  else:
                        print("생년월일을 8자리 숫자로 입력하세요.")


while True:
      soulnumber = makingsoulnumber(input("생일을 8자리 숫자로 입력하세요(종료: E): ")) #생년월일 입력, 카드 숫자 리턴
      if soulnumber == 'E':
            print("종료")
            break
      if soulnumber ==1:
          print("01. MAGICIAN \n 마법사카드는 모든 일의 출발을 의미하며, 1은 홀로 있어도 완전한 숫자로 여겨집니다.\n"
                "카드 속 마법사는 하늘과 땅을 잇는 자로, 당신의 자신감은 온전히 당신의 내면에서 비롯하는 힘입니다.\n"
                "스스로의 힘으로 천지의 이치를 깨우치는 분이니 겸손해지려 해도 그 진가는 금방 드러납니다. \n"
                "직감에 끌리는 성향은 여기에서 비롯하며, 무엇이든 배움은 빠른 편일 겁니다.\n"
                "다만 스스로를 너무 단단하게 신뢰하여, 본인의 생각을 강하게 밀어붙이는 경향이 있는 편입니다\n. '나는 틀리지 않는다'고 여기기에"
                "타인의 피드백을 받아들이기 어렵습니다.\n 주변에서는 당신이 잘난 척이 심하다고 느끼거나 당신을 질투하는 시선도 드물지는 않겠습니다.\n"
                "아무리 뛰어난 배우라 해도 무대가 없다면 빛나지 않는 법, 주변과 조화를 이루려는 노력을 멈추지 마십시오.")

      elif soulnumber ==2:
          print("02. HIGH PRIESTESS\n"
                "여사제는 지혜와 평온, 객관성을 의미합니다.\n 사제로서 당신은 말하기보다 듣기를 더 중요시하는 경향이 있으며,\n"
                "좀처럼 감정을 드러내지 않습니다. 그러나 항상 귀를 열고 세심하게 신경을 쓰는 당신은 감정을 잘 통제할 줄 알며, \n"
                "그렇기에 객관적으로 상황을 바라보지만 공감과 위로가 필요한 때에는 얼마든지 융통성을 발휘할 줄 아는 사람입니다.\n"
                "다만 내면의 이야기나 속 깊이 있는 감정은 잘 꺼내지 않기에,\n 주변에서는 당신을 다소 비밀이 많고 어려운 인물로 생각할 수 있습니다.\n"
                "속세를 초월한 듯한 분위기나 단단한 벽으로 인해 무시당한다 느끼는 이도 있을 테고\n 다소 쌀쌀맞다 느끼는 사람들도 있을 거예요.\n"
                "친해지고 싶은 사람이 있다면 조금은 마음을 열어 주세요.\n 당신이 무엇을 느끼는지 나눌 수 없다면 멀어질 수 있습니다.\n"
                "의도치 않게 주변을 상처 주는 건 아닌지 잠시 돌아봐도 좋겠습니다.")
      elif soulnumber ==3:
          print("03.THE EMPRESS\n"
                "여황제는 풍요와 여유, 편안함을 상징합니다. 당신은 군주이기에 권력과 힘을 가지고 있습니다.\n"
                "그러나 그 힘을 스스로보다는 남을 위해 쓰는 일이 더 많을 듯합니다.\n 모성애를 강하게 타고났다고 할 수 있겠습니다."
                "의도하지 않아도 남을 위하고 타인을 먼저 챙기며 배려하는 성향이 있습니다. \n"
                "다만 남을 먼저 챙기다 오히려 스스로에게 독이 되는 일인지 돌아보아야 합니다.\n"
                "여유가 없고 힘들 때조차 남을 먼저 신경쓰는 태도는 스스로를 좀먹으니까요.\n"
                "그렇게 된다면 결국 사랑하는 이들과의 관계를 오래 유지하기 어려울 거예요.\n"
                "\n 당신의 행복과 여유가 우선되어야 꾸준히 그 마음을 지속할 수 있음을 명심하세요.\n "
                "괜찮다고 말하는 게 능사는 아니랍니다. 스스로의 한계를 잘 파악하세요.")
      elif soulnumber == 4:
          print("04.THE EMPEROR\n"
                "황제는 보수적이고 권위적입니다.\n 뛰어난 카리스마와 리더십을 가졌기에 타인을 이끄는 일에 적합하지요.\n"
                "그렇기에 보다 강한 힘과 권력에 관한 열망 또한 지녔습니다.\n 강인한 성정과 단호한 태도로, 리더로 인정받는 만큼"
                "당신의 능력과 책임감 또한 확실할 거예요.\n"
                "더 높은 자리로 올라가고자 하는 의욕이 있으니 할 수 있는 일이라면 무엇이든 적극적으로 임합니다.\n"
                "\n 다만, 고집스러운 성향으로 모든 타인이 자신의 의견을 따라와야 한다고 여기기에 불화도 생길 테고,\n"
                "정한 규칙을 무리하게 밀어붙이려다 외려 일을 망친 경험도 있을 거예요."
                "\n 타인의 말에 조금이라도 귀를 기울이고,\n 의견을 피력하기 전에 속으로 셋까지 세어보고 나서 입을 여는 것도 좋은 방법입니다."
                "규칙을 지키는 것도 중요하지만, 때로는 융통성이 더 큰 힘을 발휘합니다.\n 굉장한 능력을 지녔음에도 사소한 것까지 노력하는 모습을 주변에 적극적으로 보여주세요.")
      elif soulnumber==5:
          print("05. THE HEIROPHANT\n"
                "교황은 신과 인간의 교두보입니다.\n타인과의 상호작용에 영향을 미칩니다. \n마치 태풍의 눈처럼 변화의 한복판에 눈에 띄지 않게 존재합니다.\n"
                "신의 목소리를 빌려 사람들을 교육하고 성장하도록 돕습니다.\n 타인의 변화를 유도하지만, 정작 자신은 타인의 눈에 띌 만큼 크게 변하지 않았네요.\n"
                "규칙을 중시하는 성정이면서도, 변화하고자 하는 욕구 또한 가지고 있으니 내면이 늘 긴장하고 있을 겁니다.\n "
                "타인에게 소위 '꼰대'란 평가를 듣는 게 내키지는 않을 거예요,\n 당신의 원칙과 질서에서 벗어나고 싶지 않다는 본심을 들키고 싶지 않을 테니까요."
                "자기 주관 없이 휩쓸려 다니는 걸 경계하는 정직한 성격 탓에\n 어떤 이들은 속을 알 수 없는 인물이라 여기기도 할 겁니다."
                "떄로는 자신의 선을 과감하게 벗어나는 용기를 발휘하세요.\n 그 선이 성장을 막고 있다는 걸 깨닫기만 한다면 의외로 재밌을 거예요."
                "유행하는 옷을 입고, 인스타 맛집도 한 번쯤 찾아가 보면 좋겠네요.\n 그 안에서 당신이 찾는 변화의 가능성을 발견할 수 있을지도 모르죠.  ")
      elif soulnumber ==6:
          print("06. THE LOVERS\n"
                "연인 카드는 타인과의 관계 속에서 자신의 정체성 확립을 의미합니다.\n 주변과의 조화를 추구하고, 분쟁과 갈등을 피하는 평화주의자죠.\n"
                "내면의 에너지가 안정되어 있으니 당신과 이야기하는 것을 남들도 편안하게 느낍니다.\n"
                "온화하고 사랑스러운 매력의 소유자이지만, 그 때문에 주변이 잠잠한 날이 없겠습니다.\n "
                "굳이 바라지 않아도 찾아오는 사람들은 있을 테니까요.\n 당신과 한 마디라도 해 보고, 눈에 한 번이라도 띄어 보고자 노력하는 이들로 인해"
                "쉴 틈이 없을 거예요.\n 사람들은 당신 곁에서 안정을 느끼지만, 당신은 피곤하기 그지없는 상황인 셈이죠.\n"
                "조금은 단호해질 필요가 있겠습니다.\n 무작정 곁을 내어주지 말고, 신중하게 재고 따져 보세요.\n 동호회, 모임 등을 통해 새로운 사람을 사귀기보다"
                "\n주변에 원래 있는 사람들 곁에서 에너지를 채워 보기를 권합니다.")
      elif soulnumber == 7:
          print("07.THE CHARIOT\n"
                "망설이지 않고 거침없이 나아가는 전차는 뒤를 돌아보지 않습니다.\n 당신은 과거보다는 현재와 미래를 사는 사람이군요.\n"
                "작은 머뭇거림조차 없이 돌진하기에, 배움이 빠르고 성과도 평균 이상입니다.\n 그런 모습을 보며 주변에서도 당신의 추진력만큼은 인정할 테고요.\n"
                "다만 다혈질적이고 인내심이 부족해 손해를 본 적이 몇 번 있겠습니다.\n 이직/이사가 유난히 잦고, 함께 노는 사람들도 자주 바뀌고,\n"
                "연애도 그다지 롱런하지는 못하겠네요.\n 변덕스럽고, 늘 주도권을 잡고 싶어하는 독불장군 같은 면이 좀처럼 사람들이 곁에 오래 머물지 못하는 이유입니다.\n"
                "스스로 이런 성향을 잘 다스려야 나아갈 수 있어요.\n 앞만 보고 달리려 하지 말고, 다른 이들의 목소리에 귀를 기울이세요.\n "
                "익숙함에서 비롯하는 안정감을 불안해하지 마십시오.\n 눈에 보이지 않는 성장도 있는 법입니다.\n 관점을 바꾼다면, 오히려 크게 전진할 성장제가 될 거예요.")
      elif soulnumber==8:
          print("08. STRENGTH\n"
                "힘은 때를 기다립니다.\n 삶의 모든 요소는 돌고 돌아 다시 마주치는 법이니 지금 눈 앞의 문제를 회피하지 않습니다.\n"
                "그렇기에 어떤 문제가 생기더라도 담담하게 해결할 방법을 먼저 찾으려 하겠습니다.\n 오히려 놀란 이를 다독이고 챙기는 일을 자주 하겠네요.\n"
                "설령 당신의 힘으로 감당하기 어렵더라도 피하지 않고 어떻게든 내면의 힘으로 이겨내려 노력하는 분입니다.\n"
                "그러나 자제력이 뛰어난 만큼, 스스로의 고통에는 둔감할 수 있겠습니다.\n 분명 지쳐 포기하고 싶은 순간이 있을 텐데,\n "
                "그럴 때조차  '조금만 참으면 된다'며 스스로를 몰아세우진 않으시나요? "
                "자신의 한계를 끝없이 시험할 테니 스트레스에도 취약하겠습니다. \n당장은 괜찮아 보여도 미래의 내가 감당해야 할 빚이라는 걸 명심하세요."
                "쓰러질 때까지 스스로를 몰아세우지 말고,\n 남들을 배려하는 만큼 스스로에게도 관대할 필요가 있겠습니다.\n"
                "가끔은 이기적으로 굴어도 괜찮아요.")
      elif soulnumber==9:
          print("09. THE HERMIT\n"
                "은둔자는 세상으로부터 도망쳐 지혜를 깨우치고 진리에 통달한 인물입니다.\n"
                "당신은 많은 사람과 어울리기보다는 혼자서 조용히 사색하기를 즐깁니다.\n 스스로는 물론이고 주변, 나아가 세상사에 대해 폭넓게 사색하니"
                "생각이 깊습니다.\n 이해심 또한 넓어서 어지간한 일은 화내지 않고 조용히 넘어가는 편입니다.\n"
                "이런 성향 탓에 때로는 사람들을 피해 숨기도 하겠네요.\n 모든 연락을 끊고 잠수를 타는 등의 행동을 하지는 않으셨나요?\n"
                "걱정하는 사람들을 떠올리지도 못할 만큼 지쳐,\n 심하면 학교나 직장에서도 소리소문 없이 사라질 테고 \n그렇게 조용히 일을 저지르고서 "
                "나중에 돌아갈 자리가 사라져 후회한 적도 몇 번쯤 있겠습니다.\n"
                "가까운 이들조차 버겁다면 솔직히 이야기하세요.\n 휴대폰도 멀리하며 조용히 집중하고 싶다고 말이예요.\n "
                "당신 곁을 지키는 이들을 작게나마 배려한다면,\n 후에 다시 돌아왔을 때 어색함 없이 그들의 손을 다시 잡을 수 있을 거랍니다.")
      elif soulnumber==10:
          print("10. WHEEL OF FORTUNE\n"
                "운명의 수레바퀴는 끝없이 돌며 변화를 멈추지 않습니다.\n"
                "당신은 가만히 혼자 사색하기보다는 끊임없이 배움을 추구합니다.\n 활동적이며, 새로운 것을 좋아하다 보니 관심 분야도 많아요.\n"
                "그래서 실패를 두려워하지 않습니다.\n 국내보다는 해외에 꿈이 있는 경우가 많습니다.\n"
                "다만, 모든 것이 '잘 되어야만 하기'때문에 끝없이 완벽을 추구하는 면이 있습니다.\n 스스로에게도 엄격하고 결단력이 있는 편이예요.\n"
                "그래서인지 조금은 지쳐있다는 걸 눈치채지 못하다가 무너지는 일이 종종 있을 법합니다.\n "
                "스스로를 돌아보고 챙겨주세요.\n 당신이 추구하는 모든 변화는 결국 당신을 위해서입니다.")
      elif soulnumber==11:
          print("11.JUSTICE\n"
                "정의로운 자는 공정하며, 결과에 승복합니다.\n "
                "정의란 진실과 균형의 표시입니다.\n 당신은 꽤나 투명한 사람이어서, 의도와 다르게 오해를 사는 일은 흔하지 않았을 거예요.\n"
                "원리원칙을 중시하는 면이 있어 가끔 고리타분하다는 말도 듣고는 합니다.\n "
                "겉과 속이 같은 사람이라, 사랑에 있어서는 계산적이지는 않는지 돌이켜볼 필요가 있습니다.\n 관계란 게 칼로 벤 것처럼 나눠 떨어지지 않는 물건이니까요.\n"
                "불법적인 루트로 돈을 번다거나 복권 등의 일확천금을 노리는 것은 추천하지 않습니다.\n 또한, 법률적으로 명시할 수 있는 부분은 명시해서 거래하는 게 좋겠습니다.\n")
      elif soulnumber==12:
          print("12.The HANGED MAN\n"
                "매달린 사람은 온화합니다. 또한 타인과는 다른 관점으로 세상을 볼 수 있습니다.\n"
                "당신은 쉽게 포기하지 않고 불편함을 인내하며 깨달음을 얻기 위해 노력합니다.\n 소위 '외강내강'입니다.\n"
                "타인을 위해 헌신하고 봉사하는 일을 주저하지 않습니다.\n 그래서인지 짝사랑에 빠지기 쉽습니다.\n "
                "상대가 나를 좋아하지 않아도 묵묵히 뒤에서 기다릴 수 있는 지고지순한 사랑을 가졌습니다.\n "
                "인내보다 열매가 더 달콤함을 아는 분이나,\n 외부에서 보기에는 답답하게 보일 수 있겠습니다.\n")
      elif soulnumber==13:
          print("13.DEATH\n"
                "죽음이란 그저 이별만을 뜻하지 않습니다. 완결이며, 종결입니다.\n"
                "당신은 맺고 끊음이 매우 확실합니다. 사사로운 정에 휘둘리지 않습니다.\n 그로 인해 주변에서"
                "냉정하고 차가운 사람, 이라는 평가를 듣는 건 어려운 일이 아닙니다.\n 맺고 끊음이 확실하기 때문에 한 가지를 집중해서"
                "시작하고 끊는 힘이 좋은 편입니다.\n 다만, 칼 같은 면 때문에 주변에 사람이 적어 종교에 심취하기 쉽습니다.\n"
                "때로는 답을 내지 말고 그저 기다리는 것이 방법일 때도 있음을 명심하는 게 좋겠습니다.")
      elif soulnumber==14:
          print("14.TEMPERANCE"
                "조화는 어느 쪽에도 치우치지 않고 다만 존재합니다.\n"
                "매사 공정하게 처리하려 하며, 규범을 지키고 전통을 고수하려는 성향이 강합니다.\n"
                "말을 아끼고 상황판단이 빠르며, 먼저 손대지 않고 상황을 지켜보는 지혜로움을 가졌습니다.\n 또한"
                "대화와 타협을 통해 관계를 정리하는 데 탁월하며\n 지적이고 철학적인 면 또한 가지고 있습니다.\n"
                "주연이 되기보다는 킹 메이커, 조연의 역할을 더 잘 소화하고 환경의 변화에 적응이 빠릅니다.\n"
                "다만, 다소 우유부단한 성격은 연애에 있어서 양다리를 걸치는 일을 만들 가능성이 있고\n "
                "자신의 말을 잘 하지 않는 성격으로 주변에서는 속을 알 수 없다는 평가를 들을 수 있겠습니다.\n"
                "모든 일에는 책임이 따름을 명심하는 게 좋겠습니다.")
      elif soulnumber==15:
          print("15.THE DEVIL\n "
                "악마는 현실적이고 계획적이며, 유혹에 약합니다.\n"
                "당신은 '울타리 안의 사람'에게는 진지한 걱정을 많이 하는 편입니다.\n 우직하게 의리가 있는 편이기도 하지요.\n"
                "돈을 만지고 벌어들이기도 하지만, 명예와는 거리가 먼 편입니다.\n 제법 순진한 면도 있지만 스스로의 이익을 위해서는 "
                "타인을 희생시키기도 합니다.\n 또한, 중독이나 속박에서 잘 벗어나지 못하여 무슨 일을 하든 빠져드는 경향이 있습니다.\n "
                "주변에 도움을 청하는 것을 주저하지 마십시오.")
      elif soulnumber==16:
          print("16. THE TOWER\n"
                "탑은 다만 그 곳에 존재하며, 그를 탐하는 자와 지키는 자가 항상 떠돕니다.\n"
                "당신은 삶의 굴곡이 많고, 갑작스레 흥하거나 갑작스레 망하는 일과 관련이 있습니다.\n"
                "꾸준하고 진득한 관계보다는 변화를 추구하는 성향이 강하여 주변 사람들이 시시각각 바뀌기도 하지요.\n"
                "그만큼 타인에게 많은 영향을 끼치기도 합니다.\n 상황에 따라 자신의 의견을 변화하기도 하지만 대개 본인의 생각과"
                "고집을 중시하며 그대로 실천하는 성향을 가졌습니다.\n 다만 때로 냉정하며 파괴적 성향을 드러내거나, 상황이 단절되면"
                "뒤도 돌아보지 않는 등\n 이기적인 성향이 있어 간혹 남이 잘 되는 것을 보기 싫어하는 일도 존재합니다.\n"
                "모든 일은 돌아옵니다. 마음 쓰는 것을 아끼지 마세요. ")
      elif soulnumber==17:
          print("17. THE STAR\n"
                "별은 항상 높이 떠 밝게 빛납니다.\n"
                "당신은 재주가 많고 뭐든 잘 해내는 편입니다.\n 남들과는 다른 시각으로 기발하고 독창적이며, 스스로가 생각하는 이상이"
                "높습니다\n. 종종 생각을 종잡을 수 없고 솔직하다는 평을 듣기도 합니다.\n 신뢰를 중요시하며, 타인에게 영향력이 있기를 바라기도 합니다.\n"
                "소위 4차원이라는 평가가 드물지 않습니다.\n"
                "좋게 말해 긍정적이며, 나쁘게 말하면 나는 늘 잘 될 거라는 몽상가입니다.\n"
                "다만, 항상 관심과 애정을 갈구하는 면이 있습니다.\n 사람이 좋아 보인다는 평을 많이 듣지만 밉보이면 곤란하게 만들기도 하지요.\n"
                "악의는 없으나 자기 주장이 강한 편이라 주변에서 피곤해하는 경향을 보입니다.\n"
                "녹아드는 것이 때로는 방법일 때가 있습니다.")
      elif soulnumber==18:
          print("18. THE MOON\n"
                "달은 어둠을 비추매 늘 변화합니다.\n"
                "당신은 연민과 동정심이 많습니다. 아기자기하고 사려깊으며 고결합니다.\n "
                "타인에 대한 영향력이 큰 편이며 신비로운 느낌을 줍니다.\n 따라서 조언자로서 큰 역할을 잘 해냅니다."
                "다만, 변덕이 심하고 변화를 종잡기 힘들며,\n 타인을 쉽게 믿지 않고 남들에게 드러나는 것을 싫어해 비밀이 많습니다.\n"
                "타인과의 거리 좁히기는 생각보다 즐겁습니다. 알아간다는 것을 피하지 마십시오.")
      elif soulnumber==19:
          print("19. THE SUN\n"
                "태양은 언제나 찬란합니다.\n"
                "당신은 심성이 나쁘지 못하고, 아이와 같이 순수한 면이 있습니다.\n 또한 창의적이고, 밝고 긍정적이며 관대하고 정직합니다.\n"
                "타인에게 뽐내기를 좋아하나 미워하기 힘든 사람으로, 적극적이고 열정적이며 리더십이 강합니다.\n"
                "다만, 타인에게 보여주고 싶은 마음이 급해 실수가 잦은 편입니다.\n 한 템포 쉬어가며 신중하게 하는 것이 중요합니다.\n"
                "또한 일의 시작은 크지만 마무리가 약한 면이 있으니 끝까지 밀고 나가는 힘을 기를 필요가 있겠습니다.")
      elif soulnumber==20:
          print("20. JUDGEMENT\n"
                "심판은 누구에게나 공정하며 누구도 피할 수 없습니다.\n"
                "당신은 배려심이 많고 타인에게 관심도 많아 보호자 역할을 자처합니다.\n"
                "재주가 많아 타인을 잘 돕고, 협조를 잘 하나\n 정작 본인의 실속은 챙기지 못하는 일이 종종 생깁니다.\n"
                "메인보다는 보조적 역할로\n 부족하거나 잘못된 일들을 꼼꼼히 체크하여 챙기는 편이고, \n"
                "언뜻 냉정해 보이나 알아갈수록 매력적인 사람이라는 평을 듣기 어렵지 않습니다.\n"
                "정당하다고 생각하면 최선을 다해 희생을 감수하여 진리를 드러내고자 하고,\n 억울한 것은 참지 못합니다.\n"
                "시야가 넓고 날카로워 냉철한 판단을 잘 내립니다.\n"
                "다만, 문제가 생기면 근본적으로 뜯어고치려 하는 성향이 있어\n 보수적인 문제에 집착하며 타협하지 않으려는 경향을 보입니다.\n"
                "때로는 한 발 물러서서 지켜보는 것도 방법이 될 수 있음을 상기하세요.")
      elif soulnumber==21:
          print("21. THE WORLD\n"
                "세계는 그 자체로 완전합니다.\n"
                "당신은 완벽주의적 성향이 강하여 \n어떤 상황에서든 무언가를 시작하면 끝을 봐야 하고,\n 마무리와 완성을 추구합니다.\n"
                "자기 울타리 안의 '내 사람'에 대한 애착이 강한 편이며,\n 그들에게 문제가 생기면 자신의 일처럼 해결하며 챙깁니다.\n"
                " 희생정신은 있으나 그것을 겉으로 드러내지는 않는 편이고 호불호가 명확한 편입니다.\n"
                "시야가 넓어 예술 관련 직업을 가진 사람이 많습니다.\n"
                "다만, 개인적 성향이 강하며 욕심이 많고 편향적으로 듣는 경향이 있습니다.\n"
                "당신이 아는 것보다 세상은 더 넓습니다. 더 크게 보고 더 멀리 보십시오. ")
      elif soulnumber==0:
          print("0. THE FOOL\n"
                "바보는 순수하며 깨끗합니다.\n"
                "당신은 모험심이 강하며 단순하고 천진난만하다는 평을 듣기가 쉽고,\n 다소 엉뚱한 성격으로 모성애(부성애)를 자극하기도 합니다.\n"
                "탐구와 개척정신이 강하고 긍정적이며,\n 미적 감각이 뛰어나 공부보다는 예술에 재능이 있을 것으로 생각됩니다.\n"
                "역마의 기질이 강해 여행을 좋아하고,\n 자유분방한 스타일로 구속받는 것을 싫어합니다.\n 미숙하고 부주의하다는 평을 듣기도 하지만,\n"
                "하나에 빠지면 열정적으로 임하여 주변에서 돕는 이 또한 많습니다\n."
                "다만, 현실과는 거리가 제법 멀어 이기적이라거나 '머릿속이 꽃밭'이라는 말을 듣기도 합니다.\n"
                "눈은 하늘을 보되, 발은 땅에 붙이십시오.")
