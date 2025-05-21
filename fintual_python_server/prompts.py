# File: prompts.py
from mcp.server.fastmcp.prompts import base
from typing import List

class FintualMCPPrompts:
    """Prompts implementation for Fintual MCP server"""
    
    @staticmethod
    def assets_provider_prompt(assets_provider: str) -> List[base.Message]:
        """Prompt to check if a provider is a Fintual asset administrator."""
        return [
            base.UserMessage(f"{assets_provider} es administradora de activos de Fintual?"),
        ]
    
    @staticmethod
    def conceptual_asset_prompt(provider: str) -> List[base.Message]:
        """Prompt to get conceptual assets of a provider."""
        return [
            base.UserMessage(f"Cuáles son los activos conceptuales de la administradora de activos {provider}"),
        ]
    
    @staticmethod
    def very_conservative_streep_analysis(from_date: str, to_date: str) -> List[base.Message]:
        """
        Prompt para analizar el fondo Very Conservative Streep en un rango de fechas.
        
        Args:
            from_date: Fecha de inicio del análisis (formato YYYY-MM-DD)
            to_date: Fecha de fin del análisis (formato YYYY-MM-DD)
        """
        return [
            base.UserMessage(
                f"""Analiza el rendimiento del fondo Very Conservative Streep (casi pura renta fija) 
                desde {from_date} hasta {to_date}. 
                
                Genera un análisis que incluya:
                1. Un gráfico de la evolución del valor cuota
                2. Tendencia general durante el período
                3. Volatilidad observada
                4. Comparación con el comportamiento esperado para un fondo conservador
                5. Recomendaciones para inversionistas basadas en este análisis
                
                Usa la herramienta get_very_conservative_streep para obtener los datos.
                Genera todos los graficos y datos en un Interactive Artifact. """
            ),
        ]
    
    @staticmethod
    def conservative_clooney_analysis(from_date: str, to_date: str) -> List[base.Message]:
        """
        Prompt para analizar el fondo Conservative Clooney en un rango de fechas.
        
        Args:
            from_date: Fecha de inicio del análisis (formato YYYY-MM-DD)
            to_date: Fecha de fin del análisis (formato YYYY-MM-DD)
        """
        return [
            base.UserMessage(
                f"""Analiza el rendimiento del fondo Conservative Clooney (principalmente renta fija) 
                desde {from_date} hasta {to_date}. 
                
                Genera un análisis que incluya:
                1. Un gráfico de la evolución del valor cuota
                2. Tendencia general durante el período
                3. Volatilidad observada
                4. Comparación con el comportamiento esperado para un fondo conservador
                5. Recomendaciones para inversionistas basadas en este análisis
                
                Usa la herramienta get_conservative_clooney para obtener los datos.
                
                Genera todos los graficos y datos en un Interactive Artifact. """
            ),
        ]
    
    @staticmethod
    def moderate_pit_analysis(from_date: str, to_date: str) -> List[base.Message]:
        """
        Prompt para analizar el fondo Moderate Pit en un rango de fechas.
        
        Args:
            from_date: Fecha de inicio del análisis (formato YYYY-MM-DD)
            to_date: Fecha de fin del análisis (formato YYYY-MM-DD)
        """
        return [
            base.UserMessage(
                f"""Analiza el rendimiento del fondo Moderate Pit (mezcla de renta fija y ETFs accionarios) 
                desde {from_date} hasta {to_date}. 
                
                Genera un análisis que incluya:
                1. Un gráfico de la evolución del valor cuota
                2. Tendencia general durante el período
                3. Volatilidad observada
                4. Comparación con el comportamiento esperado para un fondo moderado
                5. Recomendaciones para inversionistas basadas en este análisis
                
                Usa la herramienta get_moderate_pit para obtener los datos.
                
                Genera todos los graficos y datos en un Interactive Artifact. """
            ),
        ]
    
    @staticmethod
    def risky_norris_analysis(from_date: str, to_date: str) -> List[base.Message]:
        """
        Prompt para analizar el fondo Risky Norris en un rango de fechas.
        
        Args:
            from_date: Fecha de inicio del análisis (formato YYYY-MM-DD)
            to_date: Fecha de fin del análisis (formato YYYY-MM-DD)
        """
        return [
            base.UserMessage(
                f"""Analiza el rendimiento del fondo Risky Norris (casi solamente ETFs accionarios) 
                desde {from_date} hasta {to_date}. 
                
                Genera un análisis que incluya:
                1. Un gráfico de la evolución del valor cuota
                2. Tendencia general durante el período
                3. Volatilidad observada
                4. Comparación con el comportamiento esperado para un fondo de alto riesgo
                5. Recomendaciones para inversionistas basadas en este análisis
                
                Usa la herramienta get_risky_norris para obtener los datos.
                
                Genera todos los graficos y datos en un Interactive Artifact. """
            ),
        ]
    
    @staticmethod
    def compare_funds_analysis(from_date: str, to_date: str) -> List[base.Message]:
        """
        Prompt para comparar todos los fondos de Fintual en un rango de fechas.
        
        Args:
            from_date: Fecha de inicio del análisis (formato YYYY-MM-DD)
            to_date: Fecha de fin del análisis (formato YYYY-MM-DD)
        """
        return [
            base.UserMessage(
                f"""Compara el rendimiento de los cuatro fondos de Fintual 
                (Very Conservative Streep, Conservative Clooney, Moderate Pit y Risky Norris) 
                desde {from_date} hasta {to_date}.
                
                Genera un análisis comparativo que incluya:
                1. Un gráfico que muestre la evolución del valor cuota de los cuatro fondos
                2. Análisis de rendimiento relativo entre los fondos
                3. Análisis de volatilidad comparativa
                4. Correlación entre los fondos durante el período
                5. Recomendaciones para diferentes perfiles de inversionistas basadas en este análisis
                
                Usa las herramientas correspondientes para obtener los datos de cada fondo.
                
                Genera todos los graficos y datos en un Interactive Artifact. """
            ),
        ]