import sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]))
import eval_metrics, agent_tool_sim, poisoning_demo

class LabChecks(unittest.TestCase):
    def test_synthetic_counts_and_denominators(self):
        m=eval_metrics.evaluate(eval_metrics.read_data())
        self.assertEqual((m['all']['tp'],m['all']['fp'],m['all']['tn'],m['all']['fn']),(9,5,11,7))
        self.assertEqual(m['day']['fnr'],0.25)
        self.assertEqual(m['evening']['fnr'],0.625)
    def test_untrusted_page_cannot_authorize_email(self):
        self.assertEqual(agent_tool_sim.simulate(agent_tool_sim.MALICIOUS_PAGE,'secure')['tool_decision'],'DENIED')
        self.assertEqual(agent_tool_sim.simulate(agent_tool_sim.MALICIOUS_PAGE,'insecure')['tool_decision'],'WOULD_SEND_SIMULATED')
        self.assertFalse(agent_tool_sim.authorized_action(user_role='student',user_intent='send_approved_single_message',action='send_email',approved_recipient='assigned_student'))
    def test_label_change_is_traceable(self):
        clean,_=poisoning_demo.predict(poisoning_demo.TRAIN)
        altered=[(x,0 if ident=='D' else y,ident) for x,y,ident in poisoning_demo.TRAIN]
        dirty,_=poisoning_demo.predict(altered)
        self.assertNotEqual(clean,dirty)
if __name__=='__main__': unittest.main()
