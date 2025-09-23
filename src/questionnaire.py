import json
import os
import logging
from typing import Dict, List, Any, Optional

logger = logging.getLogger(__name__)


class AWSQuestionnaireEngine:
    """
    AWS-specific questionnaire engine for gathering architecture requirements
    """
    
    def __init__(self):
        """Initialize the questionnaire engine"""
        self.questions = []
        self._load_questions()
    
    def _load_questions(self):
        """Load questions from the JSON file"""
        try:
            # Get the path to the data directory
            current_dir = os.path.dirname(os.path.abspath(__file__))
            data_dir = os.path.join(os.path.dirname(current_dir), 'data')
            questions_file = os.path.join(data_dir, 'questionnaire.json')
            
            with open(questions_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.questions = data['questions']
            
            logger.info(f"Loaded {len(self.questions)} questions from questionnaire.json")
            
        except FileNotFoundError:
            logger.error("questionnaire.json file not found")
            self._create_default_questions()
        except json.JSONDecodeError as e:
            logger.error(f"Error parsing questionnaire.json: {e}")
            self._create_default_questions()
        except Exception as e:
            logger.error(f"Unexpected error loading questions: {e}")
            self._create_default_questions()
    
    def _create_default_questions(self):
        """Create default questions if file loading fails"""
        logger.info("Creating default questions as fallback")
        self.questions = [
            {
                "id": "industry",
                "question": "What industry best describes your organization?",
                "type": "single_choice",
                "required": True,
                "options": [
                    "Financial Services",
                    "Healthcare & Life Sciences",
                    "Retail & E-commerce",
                    "Manufacturing",
                    "Education",
                    "Government & Public Sector",
                    "Other"
                ]
            },
            {
                "id": "application_count",
                "question": "How many applications do you plan to deploy?",
                "type": "single_choice",
                "required": True,
                "options": [
                    "1-5 applications",
                    "6-20 applications",
                    "21-50 applications",
                    "50+ applications"
                ]
            },
            {
                "id": "compliance_requirements",
                "question": "Which compliance frameworks must your environment support?",
                "type": "multiple_choice",
                "required": False,
                "options": [
                    "GDPR",
                    "HIPAA",
                    "PCI DSS",
                    "SOX",
                    "ISO 27001",
                    "FedRAMP",
                    "None"
                ]
            },
            {
                "id": "security_level",
                "question": "What is your required security posture?",
                "type": "single_choice",
                "required": True,
                "options": [
                    "Standard - Basic security practices",
                    "Enhanced - Additional security controls",
                    "High - Strict security requirements",
                    "Maximum - Government/Military grade"
                ]
            },
            {
                "id": "regions",
                "question": "Which AWS regions will you primarily use?",
                "type": "multiple_choice",
                "required": True,
                "options": [
                    "US East (N. Virginia)",
                    "US West (Oregon)",
                    "Europe (Ireland)",
                    "Europe (Frankfurt)",
                    "Asia Pacific (Singapore)",
                    "Asia Pacific (Tokyo)",
                    "Other"
                ]
            }
        ]
    
    def get_questions(self) -> List[Dict[str, Any]]:
        """Get all questions"""
        return self.questions
    
    def get_question_by_id(self, question_id: str) -> Optional[Dict[str, Any]]:
        """Get a specific question by ID"""
        for question in self.questions:
            if question['id'] == question_id:
                return question
        return None
    
    def validate_answer(self, question_id: str, answer: Any) -> bool:
        """Validate an answer for a specific question"""
        question = self.get_question_by_id(question_id)
        if not question:
            return False
        
        # Check if required question has an answer
        if question.get('required', False) and not answer:
            return False
        
        # Validate based on question type
        if question['type'] == 'single_choice':
            return answer in question.get('options', [])
        elif question['type'] == 'multiple_choice':
            if not isinstance(answer, list):
                return False
            return all(choice in question.get('options', []) for choice in answer)
        elif question['type'] == 'text':
            return isinstance(answer, str)
        elif question['type'] == 'number':
            return isinstance(answer, (int, float))
        
        return True
    
    def get_conditional_questions(self, answers: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Get questions that should be shown based on previous answers"""
        # For now, return all questions
        # This can be enhanced with conditional logic based on answers
        return self.questions
    
    def get_next_question(self, current_index: int, answers: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Get the next question based on current progress and answers"""
        conditional_questions = self.get_conditional_questions(answers)
        
        if current_index < len(conditional_questions):
            return conditional_questions[current_index]
        
        return None
    
    def is_assessment_complete(self, answers: Dict[str, Any]) -> bool:
        """Check if the assessment is complete"""
        required_questions = [q for q in self.questions if q.get('required', False)]
        
        for question in required_questions:
            if question['id'] not in answers or not answers[question['id']]:
                return False
        
        return True
    
    def get_progress(self, answers: Dict[str, Any]) -> float:
        """Calculate assessment progress as a percentage"""
        total_questions = len(self.questions)
        answered_questions = len([q for q in self.questions if q['id'] in answers and answers[q['id']]])
        
        if total_questions == 0:
            return 1.0
        
        return answered_questions / total_questions