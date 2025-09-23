import logging
from typing import Dict, List, Any, Tuple

logger = logging.getLogger(__name__)


class AWSDecisionMatrix:
    """
    AWS-specific decision matrix for architecture pattern recommendations
    """
    
    def __init__(self):
        """Initialize the decision matrix with AWS architecture patterns"""
        self.patterns = {
            "single_account": {
                "name": "Single Account Architecture",
                "description": "All workloads in a single AWS account with environment separation via VPCs and security groups. Suitable for small organizations or simple workloads.",
                "use_cases": [
                    "Small organizations (< 5 applications)",
                    "Simple workloads with minimal compliance",
                    "Development/testing environments",
                    "Cost-conscious startups"
                ],
                "aws_services": [
                    "Single AWS Account",
                    "Multiple VPCs for environment separation",
                    "IAM for access control",
                    "CloudTrail for logging",
                    "Basic CloudWatch monitoring"
                ]
            },
            "multi_account_basic": {
                "name": "Multi-Account Basic Architecture",
                "description": "Separate AWS accounts for different environments (Dev, Test, Prod) with AWS Organizations for central management.",
                "use_cases": [
                    "Medium organizations (5-20 applications)",
                    "Clear environment separation needed",
                    "Basic compliance requirements",
                    "Growing development teams"
                ],
                "aws_services": [
                    "AWS Organizations",
                    "Separate accounts per environment",
                    "AWS Control Tower (optional)",
                    "IAM Identity Center",
                    "Cross-account IAM roles",
                    "Centralized CloudTrail"
                ]
            },
            "landing_zone_standard": {
                "name": "AWS Landing Zone Standard",
                "description": "AWS Control Tower based landing zone with security, logging, and networking organizational units. Industry standard for enterprise workloads.",
                "use_cases": [
                    "Enterprise organizations (20+ applications)",
                    "Multiple business units",
                    "Compliance requirements (SOX, ISO 27001)",
                    "Standardized governance needed"
                ],
                "aws_services": [
                    "AWS Control Tower",
                    "AWS Organizations with OUs",
                    "Security OU with dedicated accounts",
                    "IAM Identity Center",
                    "AWS Config Rules",
                    "GuardDuty & Security Hub",
                    "Centralized logging account"
                ]
            },
            "landing_zone_financial": {
                "name": "AWS Landing Zone - Financial Services",
                "description": "Highly regulated landing zone for financial services with strict compliance, audit trails, and data protection measures.",
                "use_cases": [
                    "Financial services organizations",
                    "PCI DSS compliance required",
                    "SOX compliance required",
                    "Strict audit and reporting needs"
                ],
                "aws_services": [
                    "AWS Control Tower with Financial Services compliance",
                    "Dedicated security accounts",
                    "AWS CloudHSM for encryption",
                    "AWS Macie for data discovery",
                    "Enhanced monitoring and alerting",
                    "Compliance automation tools"
                ]
            },
            "landing_zone_healthcare": {
                "name": "AWS Landing Zone - Healthcare",
                "description": "HIPAA-compliant landing zone for healthcare organizations with PHI protection and comprehensive audit capabilities.",
                "use_cases": [
                    "Healthcare organizations",
                    "HIPAA compliance required",
                    "Protected Health Information (PHI)",
                    "Medical device integration"
                ],
                "aws_services": [
                    "HIPAA-eligible AWS services only",
                    "End-to-end encryption",
                    "AWS KMS with customer-managed keys",
                    "Dedicated PHI handling accounts",
                    "Enhanced access logging",
                    "Business Associate Agreement (BAA)"
                ]
            },
            "landing_zone_government": {
                "name": "AWS Landing Zone - Government",
                "description": "FedRAMP compliant landing zone for government agencies with maximum security controls and audit capabilities.",
                "use_cases": [
                    "Government agencies",
                    "FedRAMP compliance required",
                    "FISMA compliance",
                    "Classified data handling"
                ],
                "aws_services": [
                    "AWS GovCloud regions",
                    "FedRAMP authorized services only",
                    "Enhanced security monitoring",
                    "Compliance automation",
                    "Detailed audit logging",
                    "US-only support personnel"
                ]
            },
            "hybrid_cloud": {
                "name": "Hybrid Cloud Architecture",
                "description": "Integration between on-premises infrastructure and AWS with secure connectivity and workload mobility.",
                "use_cases": [
                    "Legacy system modernization",
                    "Gradual cloud migration",
                    "On-premises regulatory requirements",
                    "Hybrid application architectures"
                ],
                "aws_services": [
                    "AWS Direct Connect",
                    "AWS Site-to-Site VPN",
                    "AWS Outposts (optional)",
                    "AWS Storage Gateway",
                    "Hybrid identity with AD Connector",
                    "Cross-premises monitoring"
                ]
            },
            "multi_region": {
                "name": "Multi-Region Architecture",
                "description": "Geographically distributed architecture across multiple AWS regions for disaster recovery and global reach.",
                "use_cases": [
                    "Global organizations",
                    "Disaster recovery requirements",
                    "Data residency compliance",
                    "High availability needs"
                ],
                "aws_services": [
                    "Multi-region AWS Organizations",
                    "Cross-region replication",
                    "Route 53 for DNS failover",
                    "Global Load Balancer",
                    "Cross-region backup",
                    "Regional compliance controls"
                ]
            }
        }
    
    def get_recommendation(self, answers: Dict[str, Any]) -> Dict[str, Any]:
        """Generate architecture recommendation based on assessment answers"""
        scores = {}
        
        # Calculate scores for each pattern
        for pattern_id, pattern in self.patterns.items():
            score = self._calculate_pattern_score(pattern_id, answers)
            scores[pattern_id] = score
        
        # Find the best pattern
        if scores:
            best_pattern_id = max(scores.keys(), key=lambda k: scores[k])
            best_pattern = self.patterns[best_pattern_id]
            confidence = scores[best_pattern_id]
        else:
            # Fallback to default pattern
            best_pattern_id = "landing_zone_standard"
            best_pattern = self.patterns[best_pattern_id]
            confidence = 0.5
        
        # Prepare recommendation
        recommendation = {
            "pattern": {
                "id": best_pattern_id,
                "name": best_pattern["name"],
                "description": best_pattern["description"],
                "use_cases": best_pattern["use_cases"],
                "aws_services": best_pattern["aws_services"]
            },
            "confidence": confidence,
            "industry": answers.get("industry", "General"),
            "compliance": answers.get("compliance_requirements", []),
            "reasoning": self._get_recommendation_reasoning(best_pattern_id, answers),
            "alternatives": self._get_alternative_patterns(scores, best_pattern_id)
        }
        
        return recommendation
    
    def _calculate_pattern_score(self, pattern_id: str, answers: Dict[str, Any]) -> float:
        """Calculate score for a specific pattern based on answers"""
        score = 0.0
        max_score = 0.0
        
        # Industry-specific scoring
        industry = answers.get("industry", "")
        if pattern_id == "landing_zone_financial" and "Financial" in industry:
            score += 0.3
        elif pattern_id == "landing_zone_healthcare" and "Healthcare" in industry:
            score += 0.3
        elif pattern_id == "landing_zone_government" and "Government" in industry:
            score += 0.3
        max_score += 0.3
        
        # Application count scoring
        app_count = answers.get("application_count", "")
        if "1-5" in app_count:
            if pattern_id == "single_account":
                score += 0.25
            elif pattern_id == "multi_account_basic":
                score += 0.15
        elif "6-20" in app_count:
            if pattern_id == "multi_account_basic":
                score += 0.25
            elif pattern_id == "landing_zone_standard":
                score += 0.15
        elif "21-50" in app_count or "51-100" in app_count or "100+" in app_count:
            if pattern_id == "landing_zone_standard":
                score += 0.25
            elif "financial" in pattern_id.lower() or "healthcare" in pattern_id.lower():
                score += 0.20
        max_score += 0.25
        
        # Compliance requirements scoring
        compliance = answers.get("compliance_requirements", [])
        if compliance and compliance != ["None"]:
            if pattern_id == "single_account":
                score += 0.05  # Low compliance capability
            elif pattern_id == "multi_account_basic":
                score += 0.10  # Basic compliance capability
            elif "landing_zone" in pattern_id:
                score += 0.20  # High compliance capability
                
                # Specific compliance matching
                if any("PCI" in comp for comp in compliance) and "financial" in pattern_id:
                    score += 0.05
                if any("HIPAA" in comp for comp in compliance) and "healthcare" in pattern_id:
                    score += 0.05
                if any("FedRAMP" in comp or "FISMA" in comp for comp in compliance) and "government" in pattern_id:
                    score += 0.05
        max_score += 0.20
        
        # Security level scoring
        security_level = answers.get("security_level", "")
        if "Standard" in security_level:
            if pattern_id in ["single_account", "multi_account_basic"]:
                score += 0.15
        elif "Enhanced" in security_level:
            if pattern_id == "landing_zone_standard":
                score += 0.15
        elif "High" in security_level or "Maximum" in security_level:
            if "financial" in pattern_id or "healthcare" in pattern_id or "government" in pattern_id:
                score += 0.15
        max_score += 0.15
        
        # Data residency and regional requirements
        data_residency = answers.get("data_residency", "")
        regions = answers.get("regions", [])
        
        if "multi-region" in data_residency.lower() or len(regions) > 2:
            if pattern_id == "multi_region":
                score += 0.10
        elif "EU data residency" in data_residency:
            if "landing_zone" in pattern_id:
                score += 0.05
        max_score += 0.10
        
        # Network connectivity requirements
        network_connectivity = answers.get("network_connectivity", [])
        if any("on-premises" in conn.lower() or "Direct Connect" in conn or "VPN" in conn for conn in network_connectivity):
            if pattern_id == "hybrid_cloud":
                score += 0.10
            elif "landing_zone" in pattern_id:
                score += 0.05
        max_score += 0.10
        
        # Normalize score to 0-1 range
        if max_score > 0:
            normalized_score = score / max_score
        else:
            normalized_score = 0.5  # Default score if no criteria matched
        
        return min(1.0, max(0.0, normalized_score))
    
    def _get_recommendation_reasoning(self, pattern_id: str, answers: Dict[str, Any]) -> str:
        """Generate reasoning for the recommendation"""
        reasoning = []
        
        # Industry reasoning
        industry = answers.get("industry", "")
        if "Financial" in industry and "financial" in pattern_id:
            reasoning.append("Financial services industry requires specialized compliance and security controls")
        elif "Healthcare" in industry and "healthcare" in pattern_id:
            reasoning.append("Healthcare industry requires HIPAA compliance and PHI protection")
        elif "Government" in industry and "government" in pattern_id:
            reasoning.append("Government sector requires FedRAMP compliance and enhanced security")
        
        # Application count reasoning
        app_count = answers.get("application_count", "")
        if "1-5" in app_count and pattern_id == "single_account":
            reasoning.append("Small application count suits single account architecture")
        elif "landing_zone" in pattern_id and ("21-50" in app_count or "100+" in app_count):
            reasoning.append("Large application portfolio requires enterprise landing zone structure")
        
        # Compliance reasoning
        compliance = answers.get("compliance_requirements", [])
        if compliance and compliance != ["None"]:
            reasoning.append(f"Compliance requirements ({', '.join(compliance)}) need structured governance")
        
        # Security reasoning
        security_level = answers.get("security_level", "")
        if "High" in security_level or "Maximum" in security_level:
            reasoning.append("High security requirements demand advanced controls and isolation")
        
        if not reasoning:
            reasoning.append("This pattern best matches your overall requirements and AWS best practices")
        
        return ". ".join(reasoning) + "."
    
    def _get_alternative_patterns(self, scores: Dict[str, float], best_pattern_id: str) -> List[Dict[str, Any]]:
        """Get alternative patterns ranked by score"""
        # Sort patterns by score, excluding the best one
        alternatives = [(pid, score) for pid, score in scores.items() if pid != best_pattern_id]
        alternatives.sort(key=lambda x: x[1], reverse=True)
        
        # Return top 2 alternatives
        result = []
        for pattern_id, score in alternatives[:2]:
            pattern = self.patterns[pattern_id]
            result.append({
                "name": pattern["name"],
                "description": pattern["description"],
                "confidence": score
            })
        
        return result
    
    def get_all_patterns(self) -> Dict[str, Dict[str, Any]]:
        """Get all available architecture patterns"""
        return self.patterns
    
    def get_pattern_by_id(self, pattern_id: str) -> Dict[str, Any]:
        """Get a specific pattern by ID"""
        return self.patterns.get(pattern_id, {})